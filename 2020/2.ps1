$file = Get-content -Path "1.txt"

foreach ($number in $file) {
    #Write-Host "Number is: $number"
    foreach ($number2 in $file) {
        #Write-Host "Number2 is: $number2"
        foreach ($number3 in $file) {
            $sum = [int]$number + [int]$number2 + [int]$number3
            if ($sum -eq 2020) {
                $answer = "Number1 is: $number and number2 is: $number2"
                $answer2 = [int]$number * [int]$number2 * [int]$number3
                Break
            }
            $sum = $null
        }
    }
}
$answer
$answer2