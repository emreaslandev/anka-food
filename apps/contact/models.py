from django.db import models

class Contact(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name='Ad Soyad', 
        help_text='Adınızı ve Soyadınızı giriniz.'
    )
    email = models.EmailField(
        verbose_name='E-Posta Adresi', 
        help_text='Geçerli bir e-posta adresi giriniz.',
        blank=True, 
        null=True
    )
    mobile_phone = models.CharField(
        max_length=20, 
        verbose_name='Cep Telefonu', 
        help_text='Cep telefon numaranızı giriniz.', 
        blank=True, 
        null=True
    )
    mobile_phone_2 = models.CharField(
        max_length=20, 
        verbose_name='Cep Telefonu 2', 
        help_text='Cep telefon numaranızı giriniz.', 
        blank=True, 
        null=True
    )
    mobile_phone_3 = models.CharField(
        max_length=20, 
        verbose_name='Cep Telefonu 3', 
        help_text='Cep telefon numaranızı giriniz.', 
        blank=True, 
        null=True
    )
    mobile_phone_4 = models.CharField(
        max_length=20, 
        verbose_name='Cep Telefonu 4', 
        help_text='Cep telefon numaranızı giriniz.', 
        blank=True, 
        null=True
    )
    phone = models.CharField(
        max_length=20, 
        verbose_name='Telefon Numarası', 
        help_text='Telefon numaranızı giriniz.', 
        blank=True, 
        null=True
    )
########################################################################################################################################################################
########################################################################################################################################################################
    instagram = models.URLField(
        max_length=200, 
        verbose_name='Instagram', 
        help_text='Instagram profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    instagram_k_adi = models.CharField(
        max_length=100, 
        verbose_name='Instagram Kullanıcı Adı', 
        help_text='Instagram kullanıcı adınızı giriniz.', 
        blank=True, 
        null=True
    )
########################################################################################################################################################################
########################################################################################################################################################################
    facebook = models.URLField(
        max_length=200, 
        verbose_name='Facebook', 
        help_text='Facebook profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    # facebook_k_adi = models.CharField(
    #     max_length=100, 
    #     verbose_name='Facebook Kullanıcı Adı', 
    #     help_text='Facebook kullanıcı adınızı giriniz.', 
    #     blank=True, 
    #     null=True
    # )
########################################################################################################################################################################
########################################################################################################################################################################
    twitter = models.URLField(
        max_length=200, 
        verbose_name='Twitter', 
        help_text='Twitter profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    # twitter_k_adi = models.CharField(
    #     max_length=100, 
    #     verbose_name='Twitter Kullanıcı Adı', 
    #     help_text='Twitter kullanıcı adınızı giriniz.', 
    #     blank=True, 
    #     null=True
    # )
########################################################################################################################################################################
########################################################################################################################################################################
    linkedin = models.URLField(
        max_length=200, 
        verbose_name='LinkedIn', 
        help_text='LinkedIn profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    # linkedin_k_adi = models.CharField(
    #     max_length=100, 
    #     verbose_name='LinkedIn Kullanıcı Adı', 
    #     help_text='LinkedIn kullanıcı adınızı giriniz.', 
    #     blank=True, 
    #     null=True
    # )
########################################################################################################################################################################
########################################################################################################################################################################
    youtube = models.URLField(
        max_length=200, 
        verbose_name='Youtube', 
        help_text='Youtube kanal URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    # youtube_k_adi = models.CharField(
    #     max_length=100, 
    #     verbose_name='Youtube Kullanıcı Adı', 
    #     help_text='Youtube kullanıcı adınızı giriniz.', 
    #     blank=True, 
    #     null=True
    # )
########################################################################################################################################################################
########################################################################################################################################################################    
    tiktok = models.URLField(
        max_length=200, 
        verbose_name='Tiktok', 
        help_text='Tiktok profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    # tiktok_k_adi = models.CharField(
    #     max_length=100, 
    #     verbose_name='Tiktok Kullanıcı Adı', 
    #     help_text='Tiktok kullanıcı adınızı giriniz.', 
    #     blank=True, 
    #     null=True
    # )
########################################################################################################################################################################
########################################################################################################################################################################
    address = models.CharField(
        max_length=500, 
        verbose_name='Adres', 
        help_text='Adresinizi giriniz.', 
        blank=True, 
        null=True
    )



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim Bilgileri'