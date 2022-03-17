# 🍩 Nft_donuts_generator 

# Автоматическая генерация крипто-артов с "послойным" созданием изображения.


Сначала генерируется рандомный фон из мягких RGB оттенков заданных в base.py файле. Далее Рандомно генерируется уникальный номер изображения. 
Далее последовательно перерибираются основные слои изображения и рандомно, в рамках заданного дипозона движения цвета в RGB спектре, накладываются на фон и друг на друга.

После, на основе основных слоев, генирируются участки теней изображения, также рандомно и в заданных дипозонах движения цвета в RGB спектре. Это сделано для того, чтобы изображения не выглядели слишком аляписто, и оттенки сочетались друг с другом.

Далее работает рандомайзер выпадения рарных предметов, в случае успеха происходит выбор некого предмета по категории редкости, также предмет может перекрашиваться (в зависимости от того что именно выпало) и также накладывается на получившееся изображение.

Все готовые изображения отправляются в папку result. Под каждый предмет создается своя папка с его изображением и характеристиками. В папке result/all_donuts, помещаются все изображения, для больше удобства работы с данными. Кроме того дополнительно файлы помещаются вдиректорию на ПК.

Все изображения должны быть в формате PNG. Все изображения должны быть размером 64х50.

Однако, стоит заметить, что алгоритм универсальный, можно создавать изображения любого размера, редкости, количеством слоев, вариативностью изменения цвета и т.д.
