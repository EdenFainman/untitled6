"""Eden Fainman ID 206796351
Assignment 1"""
"""
neriya the >>> d.amount()
191.18
>>>e.amount()
203.51

from what is written in the work solution isnt right..
50*3.82=191.0
50*4.07=203.5
so my code is fine.
"""
import math

rates = {('dollar', 'nis'): 3.82, ('euro', 'nis'): 4.07, ('euro', 'dollar'): 1.14, ('dollar', 'euro'): 0.88,
         ('nis', 'euro'): 0.28, ('nis', 'dollar'): 0.32}


class Shekel:
    def __init__(self, correntvalue):
        """
        constructor
        :param correntvalue: the amount of this corrency
        """
        self.__correntvalue = correntvalue

    def __str__(self):
        """

        :return: string of Shekel
        """
        return f'{float(self.__correntvalue)} nis'

    def __repr__(self):
        """

        :return: represent of Shekel
        """
        return repr(str(float(self.__correntvalue)) + 'nis')

    def getcorrentvalues(self):
        """

        :return: the amount of this corrency
        """
        return self.__correntvalue

    def amount(self):
        """

        :return: the amount of this corrency in Shekel
        """
        return self.__correntvalue

    def amountse(self):
        """

        :return: change the amount from nis to euro
        """
        return rates[('nis', 'euro')] * self.__correntvalue

    def amountsd(self):
        """

        :return: change the amount from nis to dollar
        """
        return rates[('nis', 'dollar')] * self.__correntvalue

    def __add__(self, other):
        """

        :param other: the second argument of add function
        :return: sum in shekel
        """
        return self.__correntvalue + other.amount()

    def __sub__(self, other):
        """

        :param other: the second argument of add function
        :return: Subtraction in shekel
        """
        return self.amount() - other.amount()


class Dollar:
    def __init__(self, correntvalued):
        """
        constructor
        :param correntvalue: the amount of this corrency
        """
        self.__correntvalued = correntvalued

    def __str__(self):
        """

        :return: string of Dollar
        """
        return f'{float(self.__correntvalued)}$'

    def __repr__(self):
        """

        :return: represent of dollar
        """
        return repr(str(float(self.__correntvalued)) + '$')

    def getcorrentvalued(self):
        """

        :return: the amount from this corrency
        """
        return self.__correntvalued

    def amount(self):
        """

        :return: the amount in shekel
        """
        return rates[('dollar', 'nis')] * self.__correntvalued

    def amountde(self):
        """

        :return: the amount in euro
        """
        return rates[('dollar', 'euro')] * self.__correntvalued

    def __add__(self, other):
        """

        :param other: the second argument
        :return: sum of both in shekel
        """
        return self.amount() + other.amount()

    def __sub__(self, other):
        """

        :param other: the second argument
        :return: sub of both in shekel
        """
        return self.amount() - other.amount()


class Euro:
    def __init__(self, correntvaluee):
        """
        constructor
        :param correntvaluee: the amount of corrency
        """
        self.__correntvaluee = correntvaluee

    def __str__(self):
        """

        :return: string version to euro
        """
        return f'{float(self.__correntvaluee)}€'

    def __repr__(self):
        """

        :return: representation of euro
        """
        return repr(str(float(self.__correntvaluee)) + '€')

    def getcorrentvaluee(self):
        """

        :return: the amount in euro
        """
        return self.__correntvaluee

    def amount(self):
        """

        :return: the amount in nis
        """
        return rates[('euro', 'nis')] * self.__correntvaluee

    def amounted(self):
        """

        :return: the amount in dollar
        """
        return rates[('euro', 'dollar')] * self.__correntvaluee

    def __add__(self, other):
        """

        :param other: the second argument
        :return: the sum in shekel
        """
        return self.amount() + other.amount()

    def __sub__(self, other):
        """

        :param other: the second argument
        :return: the sub is shekel
        """
        return self.amount() - other.amount()


def add(att1, att2):
    """

    :param att1: first parameter
    :param att2: second parameter
    :return: sum
    """
    return att1 + att2


def sub(att1, att2):
    """

    :param att1: first parameter
    :param att2: second parameter
    :return: sub
    """
    return att1 - att2


def isShekel(z):
    """

    :param z: corrency givven
    :return: true if shekel false is isnt
    """
    return type(z) == Shekel


def isDollar(z):
    """

    :param z: corrency givven
    :return: true if dollar false is isnt
    """
    return type(z) == Dollar


def isEuro(z):
    """

    :param z: corrency givven
    :return: true if euro false is isnt
    """
    return type(z) == Euro


def addDDtoD(dollar1, dollar2):
    """

    :param dollar1: dollar corrency
    :param dollar2: dollar corrency
    :return: sum of both in dollar
    """
    return dollar1.getcorrentvalued() + dollar2.getcorrentvalued()


def subDDtoD(dollar1, dollar2):
    """

    :param dollar1: dollar corrency
    :param dollar2: dollar corrency
    :return: sub of both in dollar
    """
    return dollar1.getcorrentvalued() + dollar2.getcorrentvalued()


def addEEtoE(euro1, euro2):
    """

    :param euro1: euro corrency
    :param euro2: euro corrency
    :return: sum of both in euro
    """
    return euro1.getcorrentvaluee() + euro2.getcorrentvaluee()


def subEEtoE(euro1, euro2):
    """

    :param euro1: euro corrency
    :param euro2: euro corrency
    :return: sub of both in euro
    """
    return euro1.getcorrentvaluee() - euro2.getcorrentvaluee()


def addSStoS(shekel1, shekel2):
    """

    :param shekel1: shekel corrency
    :param shekel2: shekel corrency
    :return: sum of both in euro
    """
    return shekel1.getcorrentvalues() + shekel2.getcorrentvalues()


def subSStoS(shekel1, shekel2):
    """

    :param shekel1: shekel corrency
    :param shekel2: shekel corrency
    :return: sub of both in euro
    """
    return shekel1.getcorrentvalues() - shekel2.getcorrentvalues()


def addDEtoD(dollar, euro):
    """

    :param dollar: dollar corrency
    :param euro: euro corrency
    :return: sum of both in dollar
    """
    return euro.amounted() + dollar.getcorrentvalued()


def subDEtoD(dollar, euro):
    """

    :param dollar: dollar corrency
    :param euro: euro corrency
    :return: sub of both in dollar
    """
    return dollar.getcorrentvalued() - euro.amounted()


def addEDtoE(euro, dollar):
    """

    :param euro: euro corrency
    :param dollar: dollar corrency
    :return: sum of both in euro
    """
    return euro.getcorrentvaluee() + dollar.amountde()


def subEDtoE(euro, dollar):
    """

    :param euro: euro corrency
    :param dollar: dollar corrency
    :return: sub of both in euro
    """
    return euro.getcorrentvaluee() - dollar.amountde()


def addEStoE(euro, shekel):
    """

    :param euro: euro corrency
    :param shekel: shekel corrency
    :return: sum of both in euro
    """
    return euro.getcorrentvaluee() + shekel.amountse()


def subEStoE(euro, shekel):
    """

    :param euro: euro corrency
    :param shekel: shekel corrency
    :return: sub of both in euro
    """
    return euro.getcorrentvaluee() - shekel.amountse()


def addSEtoS(shekel, euro):
    """

    :param shekel: shekel corrency
    :param euro: euro corrency
    :return: sum of both in shekel
    """
    return shekel.getcorrentvalues() + euro.amount()


def subSEtoS(shekel, euro):
    """

    :param shekel: shekel corrency
    :param euro: euro corrency
    :return: sub of both in shekel
    """
    return shekel.getcorrentvalues() - euro.amount()


def addDStoD(dollar, shekel):
    """

    :param dollar: dollar corrency
    :param shekel: shekel corrency
    :return: sum of both in dollar
    """
    return dollar.getcorrentvalued() + shekel.amountsd()


def subDStoD(dollar, shekel):
    """

    :param dollar: dollar corrency
    :param shekel: shekel corrency
    :return: sub of both in dollar
    """
    return dollar.getcorrentvalued() - shekel.amountsd()


def addSDtoS(shekel, dollar):
    """

    :param shekel: shekel corrency
    :param dollar: dollar corrency
    :return: sum of both in shekel
    """
    return shekel.getcorrentvalues() + dollar.amount()


def subSDtoS(shekel, dollar):
    """

    :param shekel: shekel corrency
    :param dollar: dollar corrency
    :return: sub of both in shekel
    """
    return shekel.getcorrentvalues() - dollar.amount()


def apply(action, opp1, opp2):
    """

    :param action: add or sub
    :param opp1: first corrency
    :param opp2: second corrency
    :return: the result in the first argumment corrency
    """
    if (action == 'add'):
        if (isDollar(opp1) and isEuro(opp2)):
            return str('Dollar(' + str(addDEtoD(opp1, opp2)) + ')')
        elif (isEuro(opp1) and isDollar(opp2)):
            return str('Euro(' + str(addEDtoE(opp1, opp2)) + ')')
        elif (isEuro(opp1) and isShekel(opp2)):
            return str('Euro(' + str(addEStoE(opp1, opp2)) + ')')
        elif (isShekel(opp1) and isEuro(opp2)):
            return str('nis(' + str(addSEtoS(opp1, opp2)) + ')')
        elif (isDollar(opp1) and isShekel(opp2)):
            return str('Dollar(' + str(addDStoD(opp1, opp2)) + ')')
        elif (isDollar(opp1) and isDollar(opp2)):
            return str('Dollar(' + str(addDDtoD(opp1, opp2)) + ')')
        elif (isEuro(opp1) and isEuro(opp2)):
            return str('Euro(' + str(addEEtoE(opp1, opp2)) + ')')
        elif (isShekel(opp1) and isShekel(opp2)):
            return str('nis(' + str(addSStoS(opp1, opp2)) + ')')
        else:
            return str('nis(' + str(addSDtoS(opp1, opp2)) + ')')

    elif (action == 'sub'):
        if (isDollar(opp1) and isEuro(opp2)):
            return str('Dollar(' + str(subDEtoD(opp1, opp2)) + ')')
        elif (isEuro(opp1) and isDollar(opp2)):
            return str('Euro(' + str(subEDtoE(opp1, opp2)) + ')')
        elif (isEuro(opp1) and isShekel(opp2)):
            return str('Euro(' + str(subEStoE(opp1, opp2)) + ')')
        elif (isShekel(opp1) and isEuro(opp2)):
            return str('nis(' + str(subSEtoS(opp1, opp2)) + ')')
        elif (isDollar(opp1) and isShekel(opp2)):
            return str('Dollar(' + str(subDStoD(opp1, opp2)) + ')')
        elif (isDollar(opp1) and isDollar(opp2)):
            return str('Dollar(' + str(subDDtoD(opp1, opp2)) + ')')
        elif (isEuro(opp1) and isEuro(opp2)):
            return str('Euro(' + str(subEEtoE(opp1, opp2)) + ')')
        elif (isShekel(opp1) and isShekel(opp2)):
            return str('nis(' + str(subSStoS(opp1, opp2)) + ')')
        else:
            return str('nis(' + str(subSDtoS(opp1, opp2)) + ')')


def type_tag(par):
    """

    :param par: currency parameter
    :return: the type of corrency
    """
    if isEuro(par) == True:
        return 'euro'
    elif isDollar(par) == True:
        return 'dollar'
    elif isShekel(par) == True:
        return 'nis'


coercions = {('dollar', 'nis'): Dollar.amount, ('euro', 'nis'): Euro.amount, ('nis', 'nis'): Shekel.amount,
             ('euro', 'dollar'): Dollar.amount}


def coerce_apply(operator_name, x, y):
    """

    :param operator_name: operator name sub or add
    :param x: first currency
    :param y:second currency
    :return:the result in shekels
    """
    tx = type_tag(x)
    ty = type_tag(y)
    if tx != ty:
        if (tx, ty) in coercions:
            if tx == 'nis' or ty == 'nis':
                tx = ty
                x = coercions[(tx, ty)](x)
            else:
                if (tx == 'euro'):
                    x = Euro.amount(x)
                    tx = 'nis'
                    if (tx, ty) in coercions:
                        x = coercions[(tx, ty)](x)
                        tx = ty
                    else:
                        y = coercions[(ty, tx)](y)
                        ty = tx
                else:
                    y = Euro.amount(y)
                    ty = 'nis'
                    if (ty, tx) in coercions:
                        y = coercions[(ty, tx)](y)
                        ty = tx
        elif (ty, tx) in coercions:
            if (tx == 'nis' or ty == 'nis'):
                ty, y = tx, coercions[(ty, tx)](y)
            elif (tx == 'euro'):
                x = Euro.amount(x)
                tx = 'nis'
                if (tx, ty) in coercions:
                    x = coercions[(tx, ty)](x)
                    tx = ty
            else:
                y = Euro.amount(y)
                ty = 'nis'
                if (ty, tx) in coercions:
                    y = coercions[(ty, tx)](y)
                    ty = tx
                else:
                    x = coercions[(tx, ty)](x)
                    tx = ty

    if (operator_name == 'add'):
        y=Shekel(y)
        if(type(x)==float):
            x=x
        elif(type(x)==Shekel):
            x=x.getcorrentvalues()
        return 'Shekel('+str(y.getcorrentvalues()+float(x))+')'
    else:
        y=Shekel(y)
        if(type(x)==float):
            x=x
        elif(type(x)==Shekel):
            x=x.getcorrentvalues()
        return 'Shekel('+str(float(x)-y.getcorrentvalues())+')'



s = Shekel(50)
d = Dollar(50)
e = Euro(50)
a = Dollar(20)
print(d.amount())
print(e.amount())
print(e + e)
print(d + s)
print(add(e, d))
z = eval(repr(d))
print(z)
print(s)
print(e)
"""
please pay attention, the Conversion value in the Running example are wrong and mine is right.
"""
print(apply('add', Shekel(50), Dollar(20)))
rates[('euro', 'dollar')] = 1.06
print(apply('add', Dollar(50), Dollar(20)))
print(apply('sub', Dollar(50), Euro(20)))
print(coercions[('dollar','nis')](Dollar(50)))
print(coerce_apply('add', Shekel(50), Dollar(20)))
print(coerce_apply('add', Dollar(50), Euro(20)))
print(coerce_apply('sub', Dollar(50), Euro(20)))

