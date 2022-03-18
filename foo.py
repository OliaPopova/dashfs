import pandas as pd

matr = pd.read_excel(io='data.xlsx',
                     engine='openpyxl',
                     usecols='A:O',
                     header=16,  # в excel это №5
                     nrows=14,
                     index_col=0)
norm = [0.162, 0.054, 0.45, 0.43, 0.0011, 0.86, 0.64, 0.36, 0.369, 0.048, 0.97, 0.75, 0.713, 0.51]
p0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
p0[3] = -0.005


def foo(prohodnoi_bal,normativi, kolvo_mest):

    p0[6] = kolvo_mest - norm[6]
    p0[11] = prohodnoi_bal - norm[11]
    p0[13] = normativi - norm[13]

    p1 = (matr * p0)
    p1_list = []
    p2_list = []
    p3_list = []
    p4_list = []
    p5_list = []
    for i in range(len(p1)):
        p1_list.append(p1.sum(axis=1).iloc[i])
    p2 = (matr * p1_list)
    for i in range(len(p2)):
        p2_list.append(p2.sum(axis=1).iloc[i])
    p3 = (matr * p2_list)
    for i in range(len(p3)):
        p3_list.append(p3.sum(axis=1).iloc[i])
    p4 = (matr * p3_list)
    for i in range(len(p4)):
        p4_list.append(p4.sum(axis=1).iloc[i])
    p5 = (matr * p4_list)
    for i in range(len(p5)):
        p5_list.append(p5.sum(axis=1).iloc[i])

    year_2020 = map(sum, zip(p0, norm))
    year_2020_list = list(year_2020)

    year_2021 = map(sum, zip(p1_list, year_2020_list))
    year_2021_list = list(year_2021)

    year_2022 = map(sum, zip(p2_list, year_2021_list))
    year_2022_list = list(year_2022)

    year_2023 = map(sum, zip(p3_list, year_2022_list))
    year_2023_list = list(year_2023)

    year_2024 = map(sum, zip(p4_list, year_2023_list))
    year_2024_list = list(year_2024)

    year_2025 = map(sum, zip(p5_list, year_2024_list))
    year_2025_list = list(year_2025)

    absolut2020 = [54.000, 54.000, 30.497, 4.197800, 82.455, 69.5, 31.917, 42, 83.385, 100, 31.567, 42, 433.400, 0.79028]
    absolut2021 = [52.08992, 52.08992, 28.86629, 4.17827451, 80.87016, 72.90, 30.33505, 42, 92.50437, 100, 33.72444, 42,
                   447.38074, 1.50603]
    absolut2022 = [51.16038, 51.16038, 28.08393, 4.16854585, 80.08920, 74.67, 29.57344, 42, 97.43151, 100, 34.85784, 42,
                   454.53934, 2.07903]
    absolut2023 = [50.24742, 50.24742, 27.32278, 4.15883985, 79.31579, 76.48, 28.83096, 42, 102.62109, 100, 36.02933,
                   42, 461.81248, 2.87004]
    absolut2024 = [49.35075, 49.35075, 26.58226, 4.14915644, 78.54984, 78.33, 28.10712, 42, 108.08708, 100, 372.4019,
                   42, 469.202, 3.96201]
    absolut2025 = [48.47008, 48.47008, 25.86181, 4.13949558, 77.79129, 80.23, 27.40146, 42, 113.84422, 100, 384.9175,
                   42, 476.70976, 5.46944]

    def f(x, y):
        return x * y

    absolut2020 = (list(map(f, absolut2020, year_2020_list)))
    absolut2021 = (list(map(f, absolut2021, year_2021_list)))
    absolut2022 = (list(map(f, absolut2022, year_2022_list)))
    absolut2023 = (list(map(f, absolut2023, year_2023_list)))
    absolut2024 = (list(map(f, absolut2024, year_2024_list)))
    absolut2025 = (list(map(f, absolut2025, year_2025_list)))

    list_index = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14']
    list_index = list_index + list_index + list_index + list_index + list_index + list_index

    value = absolut2020 + absolut2021 + absolut2022 + absolut2023 + absolut2024 + absolut2025

    year2020 = []
    year2021 = []
    year2022 = []
    year2023 = []
    year2024 = []
    year2025 = []

    for i in range(14):
        year2020.append('2020')
    for i in range(14):
        year2021.append('2021')
    for i in range(14):
        year2022.append('2022')
    for i in range(14):
        year2023.append('2023')
    for i in range(14):
        year2024.append('2024')
    for i in range(14):
        year2025.append('2025')
    year = year2020 + year2021 + year2022 + year2023 + year2024 + year2025

    list_fs = ['Количество поступивших в высшие учебные заведения региона в тыс',
               'Количество поступивших в средние специальные учебные заведения региона в тыс',
               'Количество трудоустроенных выпускников ВУЗов региона в тыс',
               'Численность населения региона (контингента до 35 лет) в млн',
               'Доля инновационных предприятий в экономике региона в тыс',
               'Средний балл ЕГЭ по региону',
               'Количество бюджетных мест в ВУЗах региона в тыс',
               'Число победителей и призёров Всероссийской олимпиады школьников в регионе',
               'Среднедушевой доход семьи в тыс',
               'Уровень безработицы в регионе',
               'Средняя заработная плата выпускников по направлениям в регионе в тыс',
               'Проходной балл ЕГЭ в ВУЗы',
               'Количество обучающихся в классах профильного обучения в тыс',
               'Нормативы (повышающие коэффициенты) для ВУЗов в тыс']
    list_fs = list_fs + list_fs + list_fs + list_fs + list_fs + list_fs

    mydictionary = {
        'index': list_index,
        'значение': value,
        'год': year,
        'fs': list_fs}

    # create dataframe using dictionary
    df_marks = pd.DataFrame(mydictionary)

    df = df_marks.query(" index not in ['F7', 'F12', 'F14']")
    return df
