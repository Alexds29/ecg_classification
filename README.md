# Многоклассовая классификация электрокардиограмм (ЭКГ) с применением алгоритмов машинного обучения




ВВЕДЕНИЕ.
Сердечно-сосудистые заболевания (ССЗ) являются основной причиной смерти во всем мире, от которой по оценкам каждый год умирает 17,9 млн человек. Сердечно-сосудистые заболевания представляют собой группу болезней сердца и кровеносных сосудов, в которую входят ишемическая болезнь сердца, заболевания сосудов головного мозга, ревматическая болезнь сердца и другие патологии.  Более четырех из пяти смертей от ССЗ происходит в результате инфаркта и инсульта, причем треть из этих случаев смерти носит преждевременный характер и отмечается среди людей в возрасте до 70 лет.


![image](https://user-images.githubusercontent.com/112484521/206157271-6949aab1-f6c1-4e62-bbd5-42aed14534ba.png)

Большинство клинических исследований сердечно-сосудистой системы основаны наанализе ЭКГ и изучении ряда других регистрируемых сигналов, иллюстрирующих биоэлектрическую активность сердца. К числу несомненных преимуществ такого подхода можно отнести относительную простоту, доступность, неинвазивность и достаточно высокую информативность. ЭКГ– функциональный метод исследования, суть которого заключается в определении состояния сердца и сердечно-сосудистой системы по изменениям в их
электрической активности. Этот метод исследования на сегодняшний день является самым распространенным и проводится практически во всех медицинских учреждениях.
Наибольший интерес для практического здравоохранения представляют системы для диагностики заболеваний.

ПОСТАНОВКА ЗАДАЧИ.
Целью данной работы является разработка модели машинного обучения для автоматического анализа электрокардиограмм при диагностике заболеваний сердечно-сосудистой системы.


МЕТОДЫ ИССЛЕДОВАНИЯ.
Электрокардиография до сих пор остается наиболее распространенным методом функциональной диагностики в кардиологии. В то же время, существующие компьютерные средства анализа и интерпретации ЭКГ все еще не обеспечивают требуемую достоверность результатов диагностики. Изображение эталонной ЭКГ и обозначение ее
элементов показано на рис. 1.


![image](https://user-images.githubusercontent.com/112484521/206164737-7367c5fa-7c42-435a-ad39-325d9fff7a1f.png)


На реальных ЭКГ нет четких границ между информативными фрагментами, что затрудняет их автоматическое распознавание. Реальная ЭКГ обычно наблюдается в условиях разного
рода возмущений, которые далеко не всегда могут быть сведены лишь к аддитивной помехе. При повышении соотношения сигнал-шум, происходит «размытие» информативных фрагментов из-за неравномерных изменений их продолжительности от цикла к циклу что приводит к ошибкам в измерении диагностических признаков, сосредоточенных на этих фрагментах.

Автоматический анализ ЭКГ является непростой теоретической и практической задачей. Физиологическое происхождение сигнала ЭКГ, обусловливает его недетерминированность,
разнообразие, изменчивость, нестационарность и подверженность многочисленным видам помех. Увеличение эффективности методов автоматического анализа ЭКГ сдерживается ограничениями, связанными с вычислительной мощность используемых процессоров. Это в наибольшей степени относится к аппаратуре непрерывного наблюдения, так как обработка сигналов в ней должна выполняться в реальном масштабе времени. Производительность вычислительных средств постоянно повышается, поэтому становятся востребованными такие методы обработки и анализа сигналов, применение которых в системах реального времени ранее представлялось сложно реализуемым.

Нейронная сеть – математическая парадигма моделирования поведения биологических нейронных систем. Искусственная нейронная сеть состоит из нескольких простых нелинейных
элементов – нейронов, соединенных между собой взвешенными связями – синапсами, формирующими сеть.


![image](https://user-images.githubusercontent.com/112484521/206167536-8c923631-df24-441b-b5dc-e7709fd545fd.png)


Искусственный нейрон является структурной единицей искусственной нейронной сети и представляет собой аналог биологического нейрона (рис. 2).


ОБСУЖДЕНИЕ РЕЗУЛЬТАТОВ.
С математической точки зрения искусственный нейрон – это сумматор входных сигналов, применяющий к полученной сумме простую, в общем случае, нелинейную функцию, непрерывную на всей области определения. Полученный результат посылается на единственный выход.


Искусственные нейроны могут объединяются между собой определенным образом, образуя искусственную нейронную сеть. Каждый нейрон характеризуется своим текущим состоянием по аналогии с нервными клетками головного мозга, которые могут быть возбуждены или заторможены. Нейрон обладает группой синапсов – однонаправленных входных связей, соединенных с выходами других нейронов, а также имеет аксон – выходную связь данного нейрона, с которой сигнал поступает на синапсы следующих нейронов.

Каждый синапс характеризуется величиной синаптической связи (весом связи) 𝑊𝑖. Текущее состояние нейрона определяется, как взвешенная сумма его входов:
 𝑆 = ∑ 𝑥𝑖𝑊𝑖 + 𝑊0
где: w0 — коэффициент смещения нейрона (вес единичного входа)
Выход нейрона есть функция его состояния:
𝑌 = 𝐹(𝑆).
Нелинейная функция F называется активационной и может иметь различный вид. Если нейроны сгруппированы в слои и их синапсы связаны только с нейронами в соседних слоях, то подобная структура является многослойным персептроном. Модель многослойного персептрона является наиболее популярной и широко изученной. Многослойный персептрон состоит из одного входного и одного выходного слоя, с одним или несколькими скрытыми слоями.

При обнаружении и обработке ЭКГ сигнала, в основном используются многослойные персептроны и радиально-базисные нейронные сети.
При формировании исходных данных был использован архив https://figshare.com/collections/ChapmanECG/4560497/2, содержащий структурированный массив оцифрованных записей реальных физиологических сигналов и связанных с ними данных для применения биомедицинским сообществом в исследованиях. Пример записи показан на рис. 3 (фрагмент ЭКГ этой записи показан на рис. 4).


![image](https://user-images.githubusercontent.com/112484521/206201926-2634340d-9a03-4975-a15c-b7d88bc2cf07.png)


![image](https://user-images.githubusercontent.com/112484521/206202332-c5dea40c-68f8-4e5c-8ba7-12062b4a2aa0.png)


При анализе ЭКГ учитывают следующие нормальные значения интервалов и комплексов:
1. Ширина комплекса QRS в интервале 60- 100 мс.
2. Длительность интервала QT составляет 390- 450 мс.
3. Длительность интервалов R-R одинакова или имеет разброс до 10%.
4. Длительность интервала PQ составляет 120- 200 мс.
5. Амплитуда зубца S не более 20 мм.
6. Зубец T направлен вверх в отведении I и II, но в aVR отведении – всегда будет отрицательный.
7. Зубец Р по амплитуде не более 2,5 мм, а по длительности 0,1 сек.
8. Зубец Q не шире 20- 40 мс и не глубже 1/3 зубца R


Вопрос нахождения оптимального числа нейронов скрытого слоя не имеет однозначного решения по причине отсутствия устоявшейся методики.

Выбор правильного количества нейронов в скрытых слоях является очень важным. Недостаточное число нейронов не позволит сети обучиться. Большое число нейронов приведет к
увеличению времени обучения сети, до неприемлемого значения, и к эффекту переобучения сети – сеть будет прекрасно работать на обучающей выборке, и очень плохо на входных примерах, не входящих в нее. Это происходит из-за того, что сеть будет обладать избыточными способностями к обучению и наряду со значительными для данной задачи факторами будет учитывать черты, характерные лишь для данной обучающей выборки.

По этой причине в работе использован метод, в основе которого лежит учет критериев оценки эффективности работы искусственной нейронной сети: чувствительность, специфичность и ошибка обучения.

От параметров чувствительности и специфичности алгоритма зависит достоверность классификации ритмов сердца. Чувствительность характеризует достоверность определения
аномальных эпизодов, а специфичность характеризует достоверность определения эпизодов нормального сердечного ритма.
Для нахождения оптимального числа нейронов скрытого слоя нейронной сети со структурой многослойного персептрона, необходимо произвести исследование показателей чувствительности и специфичности всех выходов сети.
Показатели чувствительности и специфичности в идеальном случае должны стремиться к 100%. В реальных условиях при решении задач диагностики система должна выбрать один из нескольких вариантов диагноза. При этом по всем вариантам диагноза желательно иметь значения критериев чувствительности и специфичности системы по всем вариантам диагноза равномерно распределенными, но не ниже порогового значения, при котором результат не может считаться достоверным.
Для обучения нейронной сети был подготовлен набор данных из 10646 эпизодов ЭКГ (обучающая выборка 50%, валидационная (тестовая) выборка 50%).
Разработанная нейронная сеть содержит 32 входных нейрона, по числу учитываемых параметров, скрытые слой с 16 и 8 нейронами, и 8 нейронов в выходном слое.

Подготовленные входные данные подаются на входной слой нейронной сети, выходной слой которой диагностирует состояние пациента: cинусовая брадикардия (Sinus Bradycardia), синусовый ритм (Sinus Rhythm), мерцательная аритмия (Atrial Fibrillation), синусовая тахикардия (Sinus Tachycardia), наджелудочковая тахикардия (Supraventricular Tachycardia), трепетание предсердий (Atrial Flutter), синус-атриум-предсердный блуждающий ритм (Sinus Atrium to Atrial Wandering Rhythm) и предсердная тахикардия (Atrial Tachycardia).

Для обучения искусственной нейронной сети был использован алгоритм обратного распространения ошибки.
Алгоритм обратного распространения ошибки (рис. 8) предполагает вычисление ошибки, как выходного слоя, так и каждого нейрона обучаемой сети, а также коррекцию весов
нейронов в соответствии с их текущими значениями.
На первом шаге данного алгоритма веса всех межнейронных связей инициализируются небольшими случайными значениями (от 0 до 1).
После инициализации весов в процессе обучения нейронной сети выполняются следующие шаги: прямое распространение сигнала; вычисление ошибки нейронов последнего слоя;
обратное распространение ошибки.
Прямое распространение сигнала производится послойно, начиная со входного слоя, при этом рассчитывается сумма входных сигналов для каждого нейрона, и при помощи функции активации генерируется отклик нейрона, который распространяется в следующий слой с учетом веса межнейронной связи.
В результате выполнения данного этапа мы получаем вектор выходных значений нейронной сети. Следующий этап обучения – вычисление ошибки нейронной сети как разницы
между ожидаемым и действительным выходными значениями.
Полученные значения ошибок распространяются от последнего, выходного слоя нейронной сети, к первому. При этом вычисляются величины коррекции весов нейронов в зависимости от текущего значения веса связи, скорости обучения и ошибки, внесенной данным нейроном.
После завершения данного этапа шаги описанного алгоритма повторяются до тех пор, пока ошибка выходного слоя не достигнет требуемого значения.
При определении выходного результата учитывается максимальное значение одного из выходных нейронов (этот сигнал интерпретируется как единица, а остальные как 0). Например, один из выходных нейронов имеет значение 0,87, если это максимальное значение в выходном слое нейронов, то оно будет интерпретировано как «1», т.е. значения других нейронов выходного слоя интерпретируется как «0».



![image](https://user-images.githubusercontent.com/112484521/206207730-7b7e7f47-606e-4953-891a-065c4c5ec3f5.png)


ВЫВОД.
Точность предложенной нейросетевой системы, проверена исследованием
на тестовой группе, составила 88%. Точность обнаружения и извлечения компонентов сигнала ЭКГ, показывает, что разработанная нейросетевая модель может быть использована для выявления заболеваний сердца у пациентов.


ПРИМЕЧАНИЕ.
Рукодство к применению проекта указано в файле application_guide.


ИСПОЛЬЗУЕМЫЕ ССЫЛКИ.
1. https://www.who.int/ru/health-topics/cardiovascular-diseases#tab=tab_1
2. https://www.who.int/ru/news-room/fact-sheets/detail/the-top-10-causes-of-death
3. https://cyberleninka.ru/article/n/ispolzovanie-neyrosetevyh-metodov-dlya-avtomaticheskogo-analiza-elektrokardiogramm-pri-diagnostike-zabolevaniy-serdechno-sosudistoy
