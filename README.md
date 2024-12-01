# warehouse
информационная система по управлению складом

#### Задачи:
- [x] CRUD Product
- [x] CRUD Units
- [x] CRUD Сounterparty
- [x] CRUD Shipment
- [x] CRUD ShippingInvoice
- [ ] CRUD Provider
- [ ] CRUD Arrival
- [ ] CRUD ArrivalInvoice
- [ ] Настроить разграничение прав доступа
- [ ] Реализовать авторизацию
- [ ] Настроить регистрацию новых сотрудников в админ панели

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

### Registration
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
