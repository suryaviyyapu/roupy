# /bin/python3

manufacturers = [
    'Asus',
    'Atheros',
    'Atcom',
    'Atel Electronics',
    'Ativa',
    'ATLANTIS',
    'Aukey',
    'Avaya',
    'AVM',
    'Aztech',
    'B-LINK',
    'Belkin',
    'Benq',
    'Billion',
    'Buffalo',
    'Cameo',
    'CastleNet',
    'CISCO',
    'Cnet CopperJet',
    'Colubris Networks',
    'Compaq',
    'Compex',
    'Comtrend',
    'Corega CopperJet',
    'Cradlepoint',
    'CREATIVE',
    'CYBERGUARD',
    'Cyberoam',
    'CyberTAN',
    'D-Link',
    'Dell',
    'Dovado',
    'DRAYTEK',
    'Dynalink',
    'Edimax',
    'Encore',
    'EnGenius',
    'Fortinet',
    'Gigabyte',
    'Hawking',
    'Huawei',
    'JCG',
    'LevelOne',
    'LevelOne',
    'LG-Ericsson',
    'Linksys',
    'Loopcomm',
    'MediaLink',
    'Mikrotik',
    'Mobotix',
    'Motorola',
    'MSI',
    'NEC',
    'Netcomm',
    'Netgear',
    'Netis',
    'Nexx',
    'Open',
    'Ovislink',
    'Planet',
    'Planex',
    'PRO-NETS',
    'Proware',
    'Proxim',
    'ReadyNet',
    'Ricoh',
    'Rosewill',
    'Ruckus Wireless',
    'SerComm',
    'Siemens',
    'Sitecom',
    'SMC',
    'Sonicwall',
    'Tecom',
    'Tenda',
    'Thomson',
    'TP-Link',
    'TRENDnet',
    'Ubiquiti Networks',
    'USRobotics',
    'WESTELL',
    'WeVO',
    'ZTE',
    'ZyXEL',
]
response = "TP-Link"
def router_manufacturer(response):
    for i in manufacturers:
        if i in response:
            return i,"Archer C50"
    else:
        return 0, 0

print(router_manufacturer(response))