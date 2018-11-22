largura = float(input("Qual a largura da parede?: "))
altura = float(input("Qual a altura da parede?: "))

area = float(largura*altura)
litros = area/2

print("Sua parede tem",largura,"X",altura," e sua área para pintura é de",
      area,"m².",
      "/n Você precisa de",litros,"litros de tinta.")
