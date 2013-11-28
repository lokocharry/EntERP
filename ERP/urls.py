from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ERP.views.home', name='home'),
    # url(r'^ERP/', include('ERP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Users.views.index'),
    url(r'^login$', 'Users.views.log_in'),
    url(r'^newUser$', 'Users.views.create_user'),
    url(r'^newClient$', 'Users.views.create_client'),
    url(r'^bills$', 'Contabilidad.views.create_bill'),
    url(r'^modifyBill$', 'Contabilidad.views.modify_bill'),
    url(r'^getBill$', 'Contabilidad.views.get_bill'),
    url(r'^listBills$', 'Contabilidad.views.get_all_bills'),
    url(r'^products$', 'Contabilidad.views.create_product'),
    url(r'^modifyProduct$', 'Contabilidad.views.modify_product'),
    url(r'^getProduct$', 'Contabilidad.views.get_product'),
    url(r'^deleteProduct$', 'Contabilidad.views.delete_product'),
    url(r'^listProducts$', 'Contabilidad.views.get_all_products'),
    url(r'^accounts$', 'Contabilidad.views.create_account'),
    url(r'^modifyAccount$', 'Contabilidad.views.modify_account'),
    url(r'^getAccount$', 'Contabilidad.views.get_account'),
    url(r'^listAccounts$', 'Contabilidad.views.get_all_accounts'),
    url(r'^subaccounts$', 'Contabilidad.views.create_subaccount'),
    url(r'^modifySubAccount$', 'Contabilidad.views.modify_subaccount'),
    url(r'^getSubAccount$', 'Contabilidad.views.get_subaccount'),
    url(r'^listSubAccounts$', 'Contabilidad.views.get_all_subaccounts'),
    url(r'^liquidations$', 'Contabilidad.views.create_liquidation'),
    url(r'^modifyLiquidation$', 'Contabilidad.views.modify_liquidation'),
    url(r'^getLiquidation$', 'Contabilidad.views.get_liquidation'),
    url(r'^listLiquidations$', 'Contabilidad.views.get_all_liquidations'),
    url(r'^jobHistory$', 'Logistica.views.create_job_history'),
    url(r'^modifyJobHistory$', 'Logistica.views.modify_job_history'),
    url(r'^getJobHistory$', 'Logistica.views.get_job_history'),
    url(r'^listJobHistorys$', 'Logistica.views.get_all_job_historys'),
    url(r'^payDiscount$', 'Logistica.views.create_pay_discount'),
    url(r'^modifyPayDiscount$', 'Logistica.views.modify_pay_discount'),
    url(r'^getPayDiscount$', 'Logistica.views.get_pay_discount'),
    url(r'^listPayDiscounts$', 'Logistica.views.get_all_pay_discounts'),
    url(r'^departments$', 'RecursosHumanos.views.create_department'),
    url(r'^modifyDepartment$', 'RecursosHumanos.views.modify_department'),
    url(r'^getDepartment$', 'RecursosHumanos.views.get_department'),
    url(r'^listDepartments$', 'RecursosHumanos.views.get_all_departments'),
    url(r'^charges$', 'RecursosHumanos.views.create_charge'),
    url(r'^modifyCharge$', 'RecursosHumanos.views.modify_charge'),
    url(r'^getCharge$', 'RecursosHumanos.views.get_charge'),
    url(r'^listCharges$', 'RecursosHumanos.views.get_all_charges'),
)
