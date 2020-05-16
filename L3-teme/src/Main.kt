import java.io.*

// pentru expresii am folosit site-ul https://regex101.com/

fun stergereSpatii(lines: String): String{
    return lines.replace("[\\t ]+".toRegex()," ")

}

fun stergereLinii(lines: String): String{
 return lines.replace("[\\n]+".toRegex(),"\n")
}

fun stergereNrPagina(lines: String): String{
    return  lines.replace("\\s+[\\t ]+\\d+([\\t ]+|\\n+)".toRegex(),"")
}

fun inlocuireDiacrtice(lines : String) : String{

    val original = arrayOf("Ă", "Â", "Î","Ș", "Ț", "ă", "â", "î", "ș", "ț")
    val normalized =  arrayOf("A", "A", "I","S", "T", "a", "a", "i", "s", "t")

    return lines.map { it -> val index = original.indexOf(it.toString())
        if (index >= 0) normalized[index] else it
    }.joinToString("")
}

fun main(){

    val lines = File("Poveste.txt").reader().readText()
    var temp = stergereNrPagina(lines)
    temp = stergereSpatii(temp)
    temp = stergereLinii(temp)
    temp = inlocuireDiacrtice(temp)
    println(temp)
}

