class Conversion:
    def celsius_a_fahrenheit(self, celsius:float) -> float:
        
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        return (celsius * 9/5) + 32

    def fahrenheit_a_celsius(self, fahrenheit:float) -> float:
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        return (fahrenheit - 32) * 5/9 
    
    def metros_a_pies(self, metros:float) -> float:
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        return (metros * (3.28084))
    
    def pies_a_metros(self, pies:float) -> float:
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        return (pies *(0.3048))
    
    def decimal_a_binario(self, decimal:int) -> str:
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """
        return (bin(decimal)[2:])
    
    def binario_a_decimal(self, binario:str) -> int:
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
        return int(binario, 2)
    
    def decimal_a_romano(self, numero:int) -> str:
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        valores =[
            (1000, "M") , (900, "CM") , (500, "D") , (400,"CD") , (100 , "C") ,
            (90, "XC") , (50 , "L") , (40, "XL") , (10, "X") , (9, "IX"), (5, "V"),
            (4, "IV") , (1, "I")
        ]

        romano = ""
        for valor, simbolo in valores:
            while numero >= valor:
                romano += simbolo
                numero -= valor 
        return romano
    
    def romano_a_decimal(self, romano:str) -> int:
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        valores = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        
        total = 0
        i = 0
        while i < len(romano):
            # Si no es el último y el actual es menor que el siguiente → resta
            if i+1 < len(romano) and valores[romano[i]] < valores[romano[i+1]]:
                total += valores[romano[i+1]] - valores[romano[i]]
                i += 2  # saltamos 2 caracteres
            else:
                total += valores[romano[i]]
                i += 1
        return total

    
    def texto_a_morse(self, texto:str) -> str:
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        Morse ={"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", 
            "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", 
            "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", 
            "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
            "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
            "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
            " ": "/"}
        texto = texto.upper()
        resultado = []

        for char in texto:
            if char in Morse:
                resultado.append(Morse[char])
            else:
                resultado.append("?")
        return " ".join(resultado)
    
    def morse_a_texto(self, morse:str) -> str:
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO
        """
        Morse ={
            ".-":"A", "-...":"B", "-.-.":"C","...":"S", "---":"O", "....":"H", ".":"E", ".-..":"L",
            ".----":"1", "..---":"2", "...--":"3", "":""
        }
        palabras = morse.split(" / ")
        texto = []
        for palabra in palabras:
            letras = palabra.split(" ")
            traducida = "".join(Morse.get(letra, "?")for letra in letras)
            texto.append(traducida)
        return " ".join(texto)
        