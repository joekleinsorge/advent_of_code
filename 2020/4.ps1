begin {
    $file = Import-Csv -Path "C:\Users\y5171.CSX\Documents\3.csv"
    $i = 0
}

process {
    $report = $file | ForEach-Object {
        $password = $_.password
        $letter = $_.letter
        $low = $_.low -1
        $high = $_.high -1

        if(($password[$low] -match $letter) -xor ($password[$high] -match $letter)){
            $passed = $true
            $i++
        }
        else {$passed = $false}

        New-Object PSObject |
        Add-Member -pass NoteProperty Password $password |
        Add-Member -pass NoteProperty Passed $passed
    }
}
end {   
    $report
    $i
}
