import numpy as np


class Encrypt:
    
    def init(self, size, M, pivi, pivj):
        self.n = size
        self.M = M
        self.i = pivi
        self.j = pivj

    # Método para imprimir los elementos de una matriz de enteros
    def imprimirMatrizInt(self, M):
        for i in range(len(M)):
            for j in range(len(M[0])):
                print((M.item(i,j)), end=' ') # Imprimir ASCII
    
    #TODO: Crear un método para calcular la inversa de la matriz
    def calcularInversa(self, n, M):
        I = np.identity(n)
        MA = np.concatenate([M,I], axis = 1)
        self.eliminacionGaussiana(n, MA)
        Minv = MA[:, n:n*2]
        return Minv
        
    
    
    def intercambiarFilas(self, index1, index2, M):
        temp = []
        temp[:] = M[index2]
        M[index2] = M[index1]
        M[index1] = temp
        return M


    def buscarPivote(self, f, idx, M):
        indiceFila = -1
        maxNum = np.inf *-1
        for i in range(idx+1, f):
            if(M[i][idx] > maxNum and M[i][idx] != 0):
                indiceFila = i
                maxNum = M[i][idx]
        return indiceFila

    def eliminacionGaussiana(self, n , M):

        for i in range(n):
            pivote = M[i][i]
            if pivote == 0:
                indicePiv = self.buscarPivote(n, i, M)
                if indicePiv == -1:
                    print("No es posible calcular la inversa de esta matriz")
                    exit(0)
                else:
                    M = self.intercambiarFilas(indicePiv, i, M)
                    pivote = M[i][i]
            
            for j in range(i+1, n):
                m = M[j,i] / pivote
                M[j,i] = 0
                for k in range(i+1, n*2):
                    M[j,k] -= m * M[i][k]
        
        for i in range(len(M)):
            div = M[i,i]
            for j in range(len(M[0])):
                M[i,j] /= div
        
        for i in reversed(range(1, n)):
            pivote = M[i][i]
            for j in range(i):
                if pivote != 0:
                    m = M[j,i] / pivote
                    M[j,i] = 0
                else:
                    print("No es posible calcular la inversa de esta matriz")
                    exit(0)
                for k in reversed(range(i+1, n*2)):
                    M[j,k] -= m * M[i][k]

    
    #TODO: Método para encriptar mensaje
    def encrypt(self, A, M):
        return np.matmul(A,M)
        

    #TODO: Método para desencriptar mensaje
    def decrypt(self, E, A):
        Ainv = self.calcularInversa(4, A)
        M = np.matmul(Ainv, E)
        message = ""
        for i in range(len(M)):
            for j in range(len(M[0])):
                if i<2:
                    message += chr(int(M[i][j]))
                else:
                    message += chr(int(M[i][j])+1)
        return message


# Definición del objeto Encrypt
objE = Encrypt()

# Cadena de 16 caracteres (Esta cadena podría variar)
message = "Mango con chamoy"
print("Mensaje: ", message)

# Convertir la cadena de entrada a una matrix de enteros   
M = np.ndarray(shape=(4,4), dtype=np.int32)

for i in range(len(M)):
    for j in range(len(M[0])):
        M[i][j] = ord(message[(len(M)*i)+j]) # Función ord convierte un char en su correspondiente ASCII

print("Matriz con el mensaje en Enteros: \n", M , "\n")

print("Mensaje con su equivalente en ASCII:")
objE.imprimirMatrizInt(M) # Imprimir elementos de la matriz
print("\n")
# Matrix invertible de 4 x 4, 16 elementos en total
A = np.array([ [-3, -3, -4, -5], 
                    [0,   1,  1,  6],
                    [4,   3,  4,  8],
                    [2,   -9, 7,  9]])
    
# Encriptar mensaje
encryption = objE.encrypt(A, M)
print("Matriz de mensaje encriptado", encryption)


# Desencriptar mensaje
decryption = objE.decrypt(encryption, A)
print("Mensaje desencriptado: ",decryption)

