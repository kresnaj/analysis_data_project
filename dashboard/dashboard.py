import streamlit as sl
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

sl.title('Hasil Analisis Kualitas Udara Statiun Nongzhanguan, China.')
sl.write('Data ini diambil dari [Github](https://github.com/marceloreis/HTI/tree/master)')
tren_polutan, korelasi_kecepatan_angin = sl.tabs(['Tren ', 'Korelasi Kecepatan Angin'])

with tren_polutan:
    main_pollutants, other_pollutants = sl.columns(2)
    with main_pollutants:
        sl.header('Polutan Utama')
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
        sl.header("Polutan Lain")
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
    sl.header('Korelasi kecepatan angin dengan Polutan Utama')
    air_quality_nongzhanguan_df = pd.read_csv('main_data.csv')
    air_quality_df = pd.DataFrame(air_quality_nongzhanguan_df)
    wspm_correlation_pollutants_columns = air_quality_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'WSPM']].corr()
    correlations = wspm_correlation_pollutants_columns

    fig = plt.figure(figsize=(12, 8))
    sb.heatmap(correlations, cmap='coolwarm')
    plt.tight_layout()
    sl.pyplot(fig)
    with sl.expander("See code"):
        code = """
        air_quality_nongzhanguan_df = pd.read_csv('main_data.csv')
        air_quality_df = pd.DataFrame(air_quality_nongzhanguan_df)
        wspm_correlation_pollutants_columns = air_quality_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'WSPM']].corr()
        correlations = wspm_correlation_pollutants_columns

        plt.figure(figsize=(12, 8))
        sb.heatmap(correlations, cmap='coolwarm')
        plt.tight_layout()
        plt.show()
        """
        sl.code(code, language='python')

sl.caption('Copyright (c) 2025, all reversed by the JOSHUA KRESNA K.')