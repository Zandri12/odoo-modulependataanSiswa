from odoo import models, fields
class siswa(models.Model):
    _name    ='pendataan.siswa'
    name     =fields.Char('S.Name' , Required=True)
    nis      =fields.Char('NIS') 
    kelas    =fields.Selection([('0','XI TKJ'), ('1', 'XI RPL1'), ('2', 'XI RPL2'), ('3', 'XI MM1'), ('4', 'XI MM2'), ('5', 'XI ADP1'), ('6', 'XI ADP2'),('7', 'XI AKT')],  string='Kelas')
    mapel    =fields.Many2many('datas.guru' ,"nip")
    nilai1   =fields.Float('Points-1')
    nilai2   =fields.Float('Points-2')
    predikat = fields.Selection(
        string=u'predikat',
        selection=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')]
    )
    keterangan = fields.Text(
        string=u'keterangan',
    )
    image = fields.Binary("Image", attachment=True,
                          help="This field holds the image used as avatar for \
        this contact, limited to 1024x1024px",)
    
    Guru     = fields.One2many('datas.guru',"T_name" ,String='Nama Guru')

     
    

class guru(models.Model):
	_name = 'datas.guru'
	T_name  =fields.Char('T_Name ' , Required=True)
	nip   =fields.Char('NIP')
	mapels =fields.Selection([('AA','PPL'), ('AB','PBO'), ('AC','BASIS DATA'), ('BA','PWPB'), ('BB','PKK'), ('BC','BINDO'), ('DA','BING'), ('DB','PKN'), ('DC','MTK')],)

 