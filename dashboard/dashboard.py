import streamlit as sl
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import datetime

sl.title('Hasil Analisis Kualitas Udara Statiun Nongzhanguan, China.')
sl.write('Data ini diambil dari [Github](https://github.com/marceloreis/HTI/tree/master)')
tren_polutan, korelasi_kecepatan_angin = sl.tabs(['Tren ', 'Korelasi Kecepatan Angin'])


with sl.sidebar:
    air_quality_nongzhanguan_df = pd.read_csv('main_data.csv')
    data = {'year': [2015, 2016, 2017, 2018, 2019, 2020]}
    air_quality_df = pd.DataFrame(data)

    min_date = datetime.date(air_quality_df["year"].min(), 1, 1)
    max_date = datetime.date(air_quality_df["year"].max(), 12, 31)
    sl.image("https://cdn.freelogovectors.net/wp-content/uploads/2021/12/kalilogolinux-freelogovectors.net_.png")
    start_date, end_date = sl.date_input(
        label='Rentang Tanggal',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


with tren_polutan:
    air_quality_nongzhanguan_df = pd.read_csv('main_data.csv')
    main_pollutants, other_pollutants = sl.columns(2)
    with main_pollutants:
        sl.header('Polutan Utama')
        tren_air_quality = air_quality_nongzhanguan_df.groupby(by=['year', 'month']).agg({
            'PM2.5': 'mean',
            'PM10': 'mean',
            'SO2': 'mean',
            'NO2': 'mean',
            'CO': 'mean',
            'O3': 'mean',
            'TEMP': 'mean',
            'PRES': 'mean',
            'DEWP': 'mean',
            'RAIN': 'mean',
            'WSPM': 'mean'
        }).apply(lambda c: c.astype(int))

        # Code 1
        main_pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
        fig = plt.figure(figsize=(8, 6))
        for pollutant in main_pollutants:
            sb.lineplot(tren_air_quality, x='year', y=pollutant, label=pollutant)
        plt.xticks(rotation=50)
        plt.legend(loc='upper right')
        plt.xlabel('Year - Month')
        plt.ylabel('Micrometer/meter^3')
        plt.grid(True)
        sl.pyplot(fig)
        with sl.expander("See code"):
            code = """
            air_quality_nongzhanguan_df = pd.read_csv('main_data.csv')

            tren_air_quality = air_quality_nongzhanguan_df.groupby(by=['year', 'month']).agg({
                'PM2.5': 'mean',
                'PM10': 'mean',
                'SO2': 'mean',
                'NO2': 'mean',
                'CO': 'mean',
                'O3': 'mean',
                'TEMP': 'mean',
                'PRES': 'mean',
                'DEWP': 'mean',
                'RAIN': 'mean',
                'WSPM': 'mean'
            }).apply(lambda c: c.astype(int))

            main_pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

            plt.figure(figsize=(8, 6))
            for pollutant in main_pollutants:
            sb.lineplot(tren_air_quality, x='year', y=pollutant, label=pollutant)
            plt.xticks(rotation=50)
            plt.legend(loc='upper right')
            plt.xlabel('Year - Month')
            plt.ylabel('Micrometer/meter^3')
            plt.grid(True)
            plt.show()"""
            sl.code(code, language='python')

    with other_pollutants:
        air_quality_nongzhanguan_df = pd.read_csv('main_data.csv')
        sl.header("Polutan Lain")
        tren_air_quality = air_quality_nongzhanguan_df.groupby(by=['year', 'month']).agg({
            'PM2.5': 'mean',
            'PM10': 'mean',
            'SO2': 'mean',
            'NO2': 'mean',
            'CO': 'mean',
            'O3': 'mean',
            'TEMP': 'mean',
            'PRES': 'mean',
            'DEWP': 'mean',
            'RAIN': 'mean',
            'WSPM': 'mean'
        }).apply(lambda c: c.astype(int))
        other_pollutants = ['TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
        fig = plt.figure(figsize=(8, 6))
        for pollutant in other_pollutants:
            sb.lineplot(tren_air_quality, x='year', y=pollutant, label=pollutant)
        plt.xticks(rotation=50)
        plt.legend(loc='upper right')
        plt.xlabel('Year - Month')
        plt.ylabel('Micrometer/meter^3')
        plt.grid(True)
        sl.pyplot(fig)

        with sl.expander("See code"):
            code = """
            air_quality_nongzhanguan_df = pd.read_csv('main_data.csv')

            tren_air_quality = air_quality_nongzhanguan_df.groupby(by=['year', 'month']).agg({
                'PM2.5': 'mean',
                'PM10': 'mean',
                'SO2': 'mean',
                'NO2': 'mean',
                'CO': 'mean',
                'O3': 'mean',
                'TEMP': 'mean',
                'PRES': 'mean',
                'DEWP': 'mean',
                'RAIN': 'mean',
                'WSPM': 'mean'
            }).apply(lambda c: c.astype(int))
        
            other_pollutants = ['TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']

            plt.figure(figsize=(8, 6))
            for pollutant in other_pollutants:
                sb.lineplot(tren_air_quality, x='year', y=pollutant, label=pollutant)
            plt.xticks(rotation=50)
            plt.legend(loc='upper right')
            plt.xlabel('Year - Month')
            plt.ylabel('Micrometer/meter^3')
            plt.grid(True)
            plt.show()"""
            sl.code(code, language='python')

with korelasi_kecepatan_angin:
    air_quality_nongzhanguan_df = pd.read_csv('main_data.csv')
    sl.header('Korelasi kecepatan angin dengan Polutan Utama')
    air_quality_df = pd.DataFrame(air_quality_nongzhanguan_df)
    wspm_correlation_pollutants_columns = air_quality_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'WSPM']].corr()
    correlations = wspm_correlation_pollutants_columns

    fig = plt.figure(figsize=(12, 8))
    sb.heatmap(correlations, annot=True, cmap='coolwarm')
    plt.tight_layout()
    sl.pyplot(fig)
    with sl.expander("See code"):
        code = """
        air_quality_nongzhanguan_df = pd.read_csv('main_data.csv')
        air_quality_df = pd.DataFrame(air_quality_nongzhanguan_df)
        wspm_correlation_pollutants_columns = air_quality_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'WSPM']].corr()
        correlations = wspm_correlation_pollutants_columns

        plt.figure(figsize=(12, 8))
        sb.heatmap(correlations, annot=True, cmap='coolwarm')
        plt.tight_layout()
        plt.show()
        """
        sl.code(code, language='python')

sl.caption('Copyright (c) 2025, all reversed by the JOSHUA KRESNA K.')