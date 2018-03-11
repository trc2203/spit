#When drinking from a bottle, especially sharing between people, is the last sip from the bottle comprised of mostly spit from previous sips?
CBs=[] #The Carman-Brown spit constant, used (for simplicity) for both the proportion of spit produced per unit of drink intaken as well as the proportion spewed of the resulting mixture in the mouth
i=0.0
while i<=1:
    i+=0.01
    CBs.append("%.2f" %i)
for CB in CBs:
    CB=float(CB)
    volumeSpit=0.0 #Running amount of spit in bottle
    volumeDrinkStart=2000 #ml Volume of drink before drinking has begun e.g. standard 2 litre bottle
    proportionDrink=1.0 #Starting proportion of drink in bottle
    volumeDrink=volumeDrinkStart*proportionDrink #Running amount of drink in bottle
    volume=volumeDrink+volumeSpit
    volumePerSip=25 #ml e.g. 25ml, the amount of liquid in a standard shot glass
    numberSips=0 #Running number of sips
    spitProducedPerSip=CB*volumePerSip #Amount of spit produced in the mouth per sip which is added to the intaken drink
    proportionSpewed=CB
    volumeMixtureSpewedPerSip=proportionSpewed*(volumePerSip+spitProducedPerSip) #The amount of the mixture of spit and drink in the mouth which is spewed back into the bottle
    volumeWithoutSpew=2000
    numberSipsWithoutSpew=volumeWithoutSpew/volumePerSip
    sipNumberModel=80-numberSipsWithoutSpew
    while volume/volumePerSip>=1:
        numberSips+=1
        sipNumberModel+=1
        volumeWithoutSpew-=25
        volumeSpit=volumeSpit+spitProducedPerSip*proportionSpewed
        volume=volume-volumePerSip+volumeMixtureSpewedPerSip
        proportionSpit=volumeSpit/volume
        spitPercentage=proportionSpit*100
    print("The volume of spit in the last sip is %gml" %volumeSpit)
    print("The number of sips was %d" %numberSips)
    print("The remaining volume is %g" %volume)
    if proportionSpit>0.5:
        print("Eureka!")
        print("The value of the Carman-Brown spit constant required for the last sip of a drink to be mostly spit for the given values is %g" %CB)
        break
    else:
        print("Relax, it's still mostly juice, the spit content for CB=%g is only %g%%" %(CB,spitPercentage))
