
import winreg

hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\OneDrive")
result = winreg.QueryValueEx(hkey, "UserFolder")

print(result[0])
