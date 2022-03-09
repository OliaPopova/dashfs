import pandas as pd
matr=pd.read_excel(io='data.xlsx',
              engine='openpyxl',
              usecols='A:O',
              header=16, # в excel это №5
              nrows=14,
              index_col=0)
norm = [0.162, 0.054, 0.45, 0.43, 0.0011, 0.86, 0.64, 0.36, 0.369, 0.048, 0.97, 0.75, 0.713, 0.51]
p0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
p0[3] = -0.005
def foo (normativi, prohodnoi_bal, kolvo_mest):
      p0[6] = kolvo_mest-norm[6]
      p0[11] = prohodnoi_bal-norm[11]
      p0[13] = normativi-norm[13]

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
      list_index = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14']
      list_index = list_index + list_index + list_index + list_index + list_index + list_index

      value = year_2020_list + year_2021_list + year_2022_list + year_2023_list + year_2024_list + year_2025_list

      while i < len(value):
            value[i] = abs(value[i])
            i = i + 1

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

      list_fs=['Количество поступивших в высшие учебные заведения региона',
                    'Количество поступивших в средние специальные учебные заведения региона',
                    'Количество трудоустроенных выпускников ВУЗов региона',
                    'Численность населения региона (контингента до 35 лет)',
                    'Доля инновационных предприятий в экономике региона',
                    'Средний балл ЕГЭ по региону',
                    'Количество бюджетных мест в ВУЗах региона',
                    'Число победителей и призёров Всероссийской олимпиады школьников в регионе',
                    'Среднедушевой доход семьи',
                    'Уровень безработицы в регионе',
                    'Средняя заработная плата выпускников по направлениям в регионе',
                    'Проходной балл ЕГЭ в ВУЗы',
                    'Количество обучающихся в классах профильного обучения',
                    'Нормативы (повышающие коэффициенты) для ВУЗов']
      list_fs=list_fs+list_fs+list_fs+list_fs+list_fs+list_fs

      mydictionary = {
            'index': list_index,
            'value': value,
            'year': year,
            'fs': list_fs}

      # create dataframe using dictionary
      df_marks = pd.DataFrame(mydictionary)

      return df_marks
