def math_question():
    answer = []
    corr_answer = ['b' , 'b', 'c', 'd','d',  'a' , 'd', 'a', 'c','a']
    score = 0

    print('1. Find the sum of 111 + 222 + 333 ?')
    print('a. 700')
    print('b. 666')
    print('c. 10')
    print('d. 100')
    answer.append(input())

    print('2. If Logx (1 / 8) = - 3 / 2, then x is equal to')
    print('a. -4')
    print('b. 4')
    print('c. 1/4')
    print('d. 10')
    answer.append(input())

    print("3. 20% of 2 is equal to")
    print('a. 20')
    print('b. 4')
    print('c. 0.4')
    print('d. 0.04')
    answer.append(input())

    print('4. If Log 4 (x) = 12, then log 2 (x / 4) is equal to')
    print('a. 11')
    print('b. 48')
    print('c. -12')
    print('d. 22')
    answer.append(input())

    print('5. The period of 2 sin x cos x is')
    print('a. 4π^2')
    print('b. 2π')
    print('c. 4π')
    print('d. π')
    answer.append(input())

    print('6. When a parabola represented by the equation y - 2x 2 = 8 x + 5 is translated 3 units to the left and 2 units up, the new parabola has its vertex at')
    print('a. (-5 , -1)')
    print('b. (-5 , -5)')
    print('c. (-1 , -3)')
    print('d. (-2 , -3)')
    answer.append(input())

    print('7. The graphs of the two linear equations a x + b y = c and b x - a y = c, where a, b and c are all not equal to zero,')
    print('a. are parallel')
    print('b. intersect at one point')
    print('c. intersect at two points')
    print('d. perpendicular')
    answer.append(input())

    print('8. The three solutions of the equation f(x) = 0 are - 4, 8, and 11. Therefore, the three solutions of the equation f(2 x) = 0 are')
    print('a. - 2, 4, and 11/2')
    print('b. - 8, 16 and 22')
    print('c. - 4, 8, and 11')
    print('d. 2, 19 / 2 and 7 / 2')
    answer.append(input())

    print('9. A school committee consists of 2 teachers and 4 students. The number of different committees that can be formed from 5 teachers and 10 students is')
    print('a. 10')
    print('b. 15')
    print('c. 2100')
    print('d. 8')
    answer.append(input())

    print('10. The population of a country increased by an average of 2% per year from 2000 to 2003. If the population of this country was 2 000 000 on December 31, 2003, then the population of this country on January 1, 2000, to the nearest thousand would have been')
    print('a. 1 846 000')
    print('b. 1 852 000')
    print('c. 1 000 000')
    print('d. 1 500 000')
    answer.append(input())
    
    for i in range(len(corr_answer)):
        if(corr_answer[i] == answer[i]):
            score += 1
    

    print('your name is -')
    print(name)
    print('your id is -')
    print(id)
    print('your score is -')
    print(score)

    print ("All correct answere are : ") 
    print ([list((i+1, corr_answer[i])) for i in range(len(corr_answer))])
    


#-------------  science  ----------------------
def science_question():
    answer = []
    corr_answer = ['a','b','a','d','c','a','b','a','a','b' ]
    score = 0

    print('1. Which of the following is used in pencils?')
    print('a. Graphite')
    print('b. Silicon')
    print('c. Charcoal')
    print('d. Phosphorous')
    answer.append(input())

    print('2. Chemical formula for water is')
    print('a. NaAlO2')
    print('b. H2O')
    print('c. Al2O3')
    print('d. CaSiO3')
    answer.append(input())

    print('3. The gas usually filled in the electric bulb is')
    print('a. nitrogen')
    print('b. hydrogen')
    print('c. carbon dioxide')
    print('d. oxygen ')
    answer.append(input())

    print('4. Which of the gas is not known as green house gas? ')
    print('a. Methane')
    print('b. Nitrous oxide')
    print('c. Carbon dioxide')
    print('d. Hydrogen')
    answer.append(input())

    print('5. The hardest substance available on earth is')
    print('a. Gold')
    print('b. Iron')
    print('c. Diamond')
    print('d. Platinum')
    answer.append(input())

    print('6. Which of the following is used as a lubricant?')
    print('a. Graphite')
    print('b. Silica')
    print('c. Iron Oxide')
    print('d. Diamond')
    answer.append(input())

    print('7. The average salinity of sea water is')
    print('a. 3%')
    print('b. 3.5%')
    print('c. 2.5%')
    print('d. 2%')
    answer.append(input())

    print('8. The element common to all acids is')
    print('a. hydrogen')
    print('b. carbon')
    print('c. sulphur')
    print('d. oxygen')
    answer.append(input())

    print('9. Carbon, diamond and graphite are together called')
    print('a. allotropes')
    print('b. isomers')
    print('c. isomorphs')
    print('d. isotopes')
    answer.append(input())

    print('10. Potassium nitrate is used in')
    print('a. medicine')
    print('b. fertiliser')
    print('c. salt')
    print('d. glass')
    answer.append(input())
    
    for i in range(len(corr_answer)):
        if(corr_answer[i] == answer[i]):
            score += 1
    

    print('your name is -')
    print(name)
    print('your id is -')
    print(id)
    print('your score is -')
    print(score)

    print ("All correct answere are : ") 
    print ([list((i+1, corr_answer[i])) for i in range(len(corr_answer))])

#-------------  physics  --------------------------

def physics_question():
    answer = []
    corr_answer = ['b','a','b','c','b','a','b','b','d', 'a' ]
    score = 0

    print('1. The absorption of ink by blotting paper involves')
    print('a. viscosity of ink')
    print('b. capillary action phenomenon')
    print('c. diffusion of ink through the blotting')
    print('d. siphon action')
    answer.append(input())

    print('2. Nuclear sizes are expressed in a unit named')
    print('a. Fermi')
    print('b. angstrom')
    print('c. newton')
    print('d. tesla')
    answer.append(input())

    print('3. Light year is a unit of')
    print('a. time')
    print('b. distance')
    print('c. light')
    print('d. intensity of light')
    answer.append(input())

    print('4. Light from the Sun reaches us in nearly')
    print('a. 2 minutes')
    print('b. 4 minutes')
    print('c. 8 minutes')
    print('d. 16 minutes')
    answer.append(input())

    print('5. Pa(Pascal) is the unit for')
    print('a. thrust')
    print('b. pressure')
    print('c. frequency')
    print('d. conductivity')
    answer.append(input())

    print('6. Metals are good conductors of electricity because')
    print('a. they contain free electrons')
    print('b. the atoms are lightly packed')
    print('c. they have high melting point')
    print('d. All of the above')
    answer.append(input())

    print('7. Sound waves in air are')
    print('a. transverse')
    print('b. longitudinal')
    print('c. electromagnetic')
    print('d. polarised')
    answer.append(input())

    print('8. Sound of frequency below 20 Hz is called')
    print('a. audio sounds')
    print('b. infrasonic')
    print('c. ultrasonic')
    print('d. supersonics')
    answer.append(input())

    print('9. Moment of inertia is')
    print('a. vector')
    print('b. scalar')
    print('c. phasor')
    print('d. tensor')
    answer.append(input())

    print('10. Sound travels at the fastest speed in')
    print('a. steel')
    print('b. water')
    print('c. air')
    print('d. vacuum')
    answer.append(input())
    
    for i in range(len(corr_answer)):
        if(corr_answer[i] == answer[i]):
            score += 1
    
    print('your name is -')
    print(name)
    print('your id is -')
    print(id)
    print('your score is -')
    print(score)

    print ("All correct answere are : ") 
    print ([list((i+1, corr_answer[i])) for i in range(len(corr_answer))])

#----------  biology  -----------------

def biology_question():
    answer = []
    corr_answer = ['a','d','a', 'c','c','d','c','b','d','b' ]
    score = 0

    print('1. Energy reserves are normally stored as')
    print('a. glycogen')
    print('b. simple sugars')
    print('c. complex sugars')
    print('d. all of these')
    answer.append(input())

    print('2. Plants receive their nutrients mainly from')
    print('a. chlorophyll')
    print('b. atmosphere')
    print('c. light')
    print('d. soil')
    answer.append(input())

    print('3. Photosynthesis generally takes place in which parts of the plant?')
    print('a. Leaf and other chloroplast bearing parts')
    print('b. stem and leaf')
    print('c. Roots and chloroplast bearing parts')
    print('d. Bark and leaf')
    answer.append(input())

    print('4. Plants synthesis protein from')
    print('a. starch')
    print('b. sugar')
    print('c. amino acids')
    print('d. fatty acids')
    answer.append(input())

    print('5. Plants absorb most part of water needed by them through their')
    print('a. embryonic zone')
    print('b. growing point')
    print('c. root hairs')
    print('d. zone of elongation')
    answer.append(input())

    print('6. Photo-oxidation is')
    print('a. photorespiration')
    print('b. photolysis')
    print('c. light and oxygen induced breakdown')
    print('d. All of the above')
    answer.append(input())

    print('7. Process of cell division can take place by')
    print('a. heterosis')
    print('b. fusion')
    print('c. mitosis')
    print('d. None of these')
    answer.append(input())

    print('8. Most highly intelligent mammals are')
    print('a. whales')
    print('b. dolphins')
    print('c. elephants')
    print('d. kangaroos')
    answer.append(input())

    print('9. Prokaryotic cells lack')
    print('a. nucleolus')
    print('b. nuclear membrane')
    print('c. membrane bound by organelles')
    print('d. All of these')
    answer.append(input())

    print('10. Photosynthesis takes place faster in')
    print('a. yellow light')
    print('b. white light')
    print('c. red light')
    print('d. darkness')
    answer.append(input())
    
    for i in range(len(corr_answer)):
        if(corr_answer[i] == answer[i]):
            score += 1
    
    print('your name is -')
    print(name)
    print('your id is -')
    print(id)
    print('your score is -')
    print(score)

    print ("All correct answere are : ") 
    print ([list((i+1, corr_answer[i])) for i in range(len(corr_answer))])

#---------------------------


name = input('enter your name : ')
id = int(input('enter your id : '))
print()   
print('1.science')
print('2.physics')
print('3.biology')
print('4.math')
print()

option = int(input())

if(option==1):

    science_question()
elif(option==2):
    physics_question()

elif(option==3):
    biology_question()

elif (option==4):
    math_question()

else:
    print("wrong input")
