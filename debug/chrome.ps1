#!/usr/bin/env pwsh

function findChromePath {
    param (
        [string]$FileName
    )
    $str = reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ /s /f \chrome.exe | findstr Default
    # regex to find the drive letter until $FileName
    if ($str -match "[A-Z]\:.+$FileName") {
        return @{
            success = $true
            path = $Matches[0]
        }
    }
    else {
        return @{
            success = $false
            path = ""
        }
    }
}

$chrome = findChromePath "chrome.exe"

if ($chrome.success = $true) {
    $chrome.path
} else {
    Write-Output "Please download chrome"
}
