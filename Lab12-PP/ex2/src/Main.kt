import java.time.LocalDate
import java.time.format.DateTimeFormatter

fun String.conversie(formatter: DateTimeFormatter): LocalDate {
    return LocalDate.parse(this, formatter)
}

fun main(){
    println("14/02/2018".conversie(DateTimeFormatter.ofPattern("dd/MM/yyyy")))
    println("December 21, 2020".conversie(DateTimeFormatter.ofPattern("MMMM dd, yyyy")))
}