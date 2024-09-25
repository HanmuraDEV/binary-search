busquedaBinaria <- function(A, primero, ultimo, x){
    if (primero > ultimo){
        return(-1)
    }

    mitad <- floor((primero + ultimo) / 2)
    
    cat("primero:", primero, "ultimo:", ultimo, "mitad:", mitad, "\n")

    if(x == A[mitad]){
        return(mitad)
    }
    if(x < A[mitad]){
        return (busquedaBinaria(A, primero, mitad - 1, x))
    } else {
        return (busquedaBinaria(A, mitad + 1,ultimo, x))
    }

}

A <- c(2,4,5,6,8,11,16)
primero <- 1
ultimo <- length(A)
x <- 2

busquedaBinaria(A, primero, ultimo, x)
