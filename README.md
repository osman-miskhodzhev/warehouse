# warehouse
информационная система по управлению складом

#### Задачи:
- [x] CRUD Product
- [x] CRUD Units
- [x] CRUD Сounterparty
- [x] CRUD Shipment
- [x] CRUD ShippingInvoice
- [x] CRUD Provider
- [x] CRUD Upload
- [x] CRUD UploadInvoice
- [ ] Настроить разграничение прав доступа
- [ ] Реализовать авторизацию
- [ ] Настроить регистрацию новых сотрудников в админ панели
- [ ] Апельсины	10	ящик - реализовать склонение 

## Модель бд и распределение про приложениям:

### Products
Product
- id
- name
- quantity
- units (Связь с таблицей Units)

Units
- id
- name

### shipping
Сounterparty
- id
- name

Shipment
- id
- ShippingInvoice_id
- Product_id

ShippingInvoice
- id
- Conterparty_id

### Upload
Provider
- id
- name

Arrival
- id
- ArrivalInvoice_id
- Product_id

ArrivalInvoice
- id
- Provider_id
