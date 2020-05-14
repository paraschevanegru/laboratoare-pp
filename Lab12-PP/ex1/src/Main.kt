fun Int.primeNumber(): Boolean {
    for (i in 2..this / 2) {
        if (this% i == 0) {
            return false
        }
    }
    return true
}


fun main() {
    // true indica ca numarul e prim, iar false ca numarul nu e prim
    println(17.primeNumber())
    println(23.primeNumber())
    println(9.primeNumber())
    println(15.primeNumber())

}