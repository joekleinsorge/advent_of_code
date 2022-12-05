begin {
    $file = Import-Csv -Path "C:\Users\y5171.CSX\Documents\3.csv"
    $i = 0
}

process {
    $report = $file | ForEach-Object {
        $password = $_.password
        $letter = $_.letter
        $low = $_.low
        $high = $_.high
        $charCount = ($password.ToCharArray() | Where-Object {$_ -eq $letter} | Measure-Object).Count

        if(($charCount -ge $low) -and ($charCount -le $high)){
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
