# Многоклассовая классификация электрокардиограмм (ЭКГ) с применением методов машинного обучения




ВВЕДЕНИЕ.
Сердечно-сосудистые заболевания (ССЗ) являются основной причиной смерти во всем мире, от которой по оценкам каждый год умирает 17,9 млн человек. Сердечно-сосудистые заболевания представляют собой группу болезней сердца и кровеносных сосудов, в которую входят ишемическая болезнь сердца, заболевания сосудов головного мозга, ревматическая болезнь сердца и другие патологии.  Более четырех из пяти смертей от ССЗ происходит в результате инфаркта и инсульта, причем треть из этих случаев смерти носит преждевременный характер и отмечается среди людей в возрасте до 70 лет.


![image](https://user-images.githubusercontent.com/112484521/206157271-6949aab1-f6c1-4e62-bbd5-42aed14534ba.png)

Большинство клинических исследований сердечно-сосудистой системы основаны наанализе ЭКГ и изучении ряда других регистрируемых сигналов, иллюстрирующих биоэлектрическую активность сердца. К числу несомненных преимуществ такого подхода можно отнести относительную простоту, доступность, неинвазивность и достаточно высокую информативность. ЭКГ– функциональный метод исследования, суть которого заключается в определении состояния сердца и сердечно-сосудистой системы по изменениям в их
электрической активности. Этот метод исследования на сегодняшний день является самым распространенным и проводится практически во всех медицинских учреждениях.
Наибольший интерес для практического здравоохранения представляют системы для диагностики заболеваний.

ПОСТАНОВКА ЗАДАЧИ.
Целью данной работы является разработка модели машинного обучения для автоматического анализа электрокардиограмм при диагностике заболеваний сердечнососудистой системы.


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
При формировании исходных данных был использован архив https://figshare.com/collections/ChapmanECG/4560497/2, содержащий структурированный массив оцифрованных записей реальных физиологических сигналов и связанных с
ними данных для применения биомедицинским сообществом в исследованиях. Пример записи показан на рис. 3 (фрагмент ЭКГ этой записи показан на рис. 4).
