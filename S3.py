# Tasas de cambio fijas al 01-09-2024
TASAS_CAMBIO = {
    'USD': 0.0011,
    'VES': 0.04010,
    'EUR': 0.00099
}

TASA_COMISION = 0.001

def calcular_comision_y_valor_final(monto_clp):
    comision = monto_clp * TASA_COMISION
    valor_final = monto_clp - comision
    return comision, valor_final

def convertir_monedas(monto_clp):
    return {moneda: monto_clp * tasa for moneda, tasa in TASAS_CAMBIO.items()}

def generar_comprobante(emisor, beneficiario, monto_clp, comision, conversiones, valor_final, estado):
    return f"""
    
    COMPROBANTE DE TRANSACCIÓN
    
    Emisor: {emisor}
    Beneficiario: {beneficiario}
    
    Monto Original (CLP): {monto_clp:.2f}
    Comisión (0.10%): {comision:.2f}
    
    Conversiones:
    Dólares Americanos (USD): {conversiones['USD']:.2f}
    Bolívares (VES): {conversiones['VES']:.2f}
    Euros (EUR): {conversiones['EUR']:.2f}
    
    Valor Final (CLP): {valor_final:.2f}
    
    Estado de la Solicitud: {estado}
    """

def procesar_solicitud(monto_clp):
    return "Aprobado" if monto_clp > 0 else "Rechazado"

def main():
    emisor = input("Ingrese el nombre del emisor: ")
    beneficiario = input("Ingrese el nombre del beneficiario: ")
    monto_clp = float(input("Ingrese el monto en pesos chilenos: "))
    
    estado_solicitud = procesar_solicitud(monto_clp)
    
    if estado_solicitud == "Aprobado":
        comision, valor_final = calcular_comision_y_valor_final(monto_clp)
        conversiones = convertir_monedas(monto_clp)
        
        comprobante = generar_comprobante(emisor, beneficiario, monto_clp, comision, conversiones, valor_final, estado_solicitud)
        print(comprobante)
        
        with open('comprobante.txt', 'w') as archivo:
            archivo.write(comprobante)
    else:
        print(f"La solicitud ha sido {estado_solicitud}. No se generará comprobante.")

if __name__ == "__main__":
    main()
