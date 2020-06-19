import azs_prime
import berkut
import energia
import lukoil
import gasprom_1
import gasprom_2
import times


def update():
      print('---------------------')
      print('------АЗС Прайм------'
            '\n')
      azs_prime.run_prime()
      print('---------------------')
      print('------АЗС Беркут-----'
            '\n')
      berkut.run_berkut()
      print('---------------------')
      print('------АЗС Лукойл----- '
            '\n')
      lukoil.run_lukoil()
      print('---------------------')
      print('---АЗС Газпром(АК)---'
            '\n')
      gasprom_1.run_gasprom_1()
      print('---------------------')
      print('------АЗС Газпром----'
            '\n')
      gasprom_2.run_gasprom_2()
      print('---------------------')
      print('-------АЗС Тайм------'
            '\n')
      times.run_time()
      print('---------------------')
      print('-----АЗС Энергия-----'
            '\n')
      energia.run_energia()
      print('---------------------')

update()