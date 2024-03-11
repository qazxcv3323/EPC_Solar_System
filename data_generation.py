import pandas as pd
import numpy as np

def adjust_values_by_time(hour, mean_value, peak_value):
    """
    시간대에 따라 값을 조정하는 함수. 주간에는 peak_value를, 야간에는 mean_value의 일부를 사용합니다.
    """
    if 6 <= hour <= 18:
        return peak_value * np.sin(np.pi * (hour - 6) / 12)
    else:
        return mean_value * 0.1

def generate_detailed_solar_data(start_date, end_date):
    data_list = []
    num_days = (end_date - start_date).days + 1

    for day in range(num_days):
        date = start_date + pd.Timedelta(days=day)
        for hour in range(24):
            datetime = pd.Timestamp(date.year, date.month, date.day, hour)
            temperature = np.random.normal(25, 5)
            humidity = np.random.normal(50, 10)
            rainfall = np.random.choice([0, 0, 0, 1, 2, 5, 10], p=[0.7, 0.1, 0.1, 0.05, 0.02, 0.02, 0.01])
            DHI = np.random.normal(80, 30)
            DNI = np.random.normal(300, 100)
            pv_current = np.random.normal(8, 2)
            plant_current = np.random.normal(80, 20)
            plant_voltage = np.random.normal(400, 100)
            power = pv_current * plant_voltage  # 실제 발전량 계산
            sunshine_duration = adjust_values_by_time(hour, 0, 1) * 12  # 일조 시간 계산
            atmospheric_clarity = np.random.normal(0.75, 0.1)
            panel_orientation = np.random.choice(['South', 'East', 'West'], p=[0.7, 0.15, 0.15])
            albedo = np.random.normal(0.3, 0.05)
            age = np.random.choice(range(1, 21))
            maintenance = np.random.choice(['Good', 'Average', 'Poor'], p=[0.6, 0.3, 0.1])
            climate_change_effect = np.random.choice(['None', 'Low', 'Moderate', 'High'], p=[0.7, 0.2, 0.08, 0.02])
            grid_integration = np.random.choice(['Integrated', 'Isolated'], p=[0.8, 0.2])
            defect = 1 if rainfall > 10 or maintenance == 'Poor' else 0  # 결함 조건 설정

            data_list.append({
                "datetime": datetime,               # 날짜와 시간
                "temperature": temperature,         # 온도 (°C)
                "humidity": humidity,               # 상대 습도 (%)
                "rainfall": rainfall,               # 강수량 (mm)
                "DHI": DHI,                         # 확산 일사량 (W/m^2), 태양광이 대기에 의해 산란되어 지표에 도달하는 빛의 양
                "DNI": DNI,                         # 직접 일사량 (W/m^2), 태양으로부터 직접적으로 받는 빛의 양
                "pv_current": pv_current,           # 태양광 패널 전류 (A), 태양광 패널이 생성하는 전류의 양
                "plant_current": plant_current,     # 발전소 전류 (A), 발전소 전체에서 생성되는 전류의 양
                "plant_voltage": plant_voltage,     # 발전소 전압 (V), 발전소 전체의 전압
                "power": power,                     # 발전량 (W), 발전소에서 생성되는 전력의 양
                "sunshine_duration": sunshine_duration,         # 일조 시간 (시간), 태양 빛이 지표에 도달하는 시간의 길이
                "atmospheric_clarity": atmospheric_clarity,     # 대기 맑음 정도, 대기의 투명도나 맑음 정도를 나타냄
                "panel_orientation": panel_orientation,         # 패널 방향, 태양광 패널이 설치된 방향 (남, 동, 서)
                "albedo": albedo,                               # 지표 반사율, 지표에서 반사되는 태양광의 비율
                "age": age,                                     # 패널 나이 (년), 태양광 패널이 사용된 기간
                "maintenance": maintenance,                     # 유지보수 상태, 패널의 유지보수 상태 (좋음, 보통, 나쁨)
                "climate_change_effect": climate_change_effect, # 기후 변화 영향, 기후 변화가 발전소에 미치는 영향 정도
                "grid_integration": grid_integration,           # 그리드 통합 여부, 발전소가 전력망에 통합되어 있는지 여부
                "defect": defect                                # 결함 여부, 발전소나 패널에 결함이 있는지 여부 (0: 정상, 1: 결함)
            })


    return pd.DataFrame(data_list)

# 데이터 생성 범위 설정
start_date = pd.to_datetime("2015-01-01")
end_date = pd.to_datetime("2024-02-28")

# 데이터 생성
detailed_solar_data = generate_detailed_solar_data(start_date, end_date)

# 첫 5개 데이터 확인
print(detailed_solar_data.head())

# 데이터 저장
detailed_solar_data.to_csv("C:/Users/typar/OneDrive/바탕 화면/개인/방송대/태양광/f_solar_data.csv", index=False)
