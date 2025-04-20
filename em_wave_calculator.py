# 파일 이름: em_wave_calculator.py

import streamlit as st

def electromagnetic_wave_type(value, unit='Hz'):
    c = 3e8  # 빛의 속도 (m/s)

    if unit == 'Hz':
        freq = value
        wavelength = c / freq
    else:
        wavelength = value
        freq = c / wavelength

    # 분류
    if freq < 3e9:
        wave_type = "라디오파"
    elif freq < 3e11:
        wave_type = "마이크로파"
    elif freq < 4e14:
        wave_type = "적외선"
    elif freq < 8e14:
        wave type = "가시광선"
    elif freq < 3e16:
        wave_type = "자외선"
    elif freq < 3e19:
        wave_type = "X선"
    else:
        wave_type = "감마선"

    return freq, wavelength, wave_type

st.title("📡 전자기파 계산기")

unit = st.radio("입력 단위 선택", ['Hz (주파수)', 'm (파장)'])
value = st.number_input("값을 입력하세요:", min_value=1e-12, format="%.3e")

if st.button("계산하기"):
    input_unit = 'Hz' if unit.startswith('Hz') else 'm'
    freq, wavelength, wave_type = electromagnetic_wave_type(value, input_unit)

    st.success(f"📊 결과")
    st.write(f"✅ 전자기파 종류: **{wave_type}**")
    st.write(f"📶 주파수: {freq:.3e} Hz")
    st.write(f"🌊 파장: {wavelength:.3e} m")
