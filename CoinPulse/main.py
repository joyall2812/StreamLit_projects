import streamlit as st
from forex_python.converter import CurrencyRates
c=CurrencyRates()
st.title('COIN :red[PULSE!!]')
st.header('CURRENCY :red[CONVERTER]')


# List of currency codes
currency_codes = ['EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF',
                  'ISK', 'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'INR', 'KRW',
                  'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR', 'USD']

# Mapping of currency codes to full names
currency_names = {
    'EUR': 'Euro',
    'JPY': 'Japanese Yen',
    'BGN': 'Bulgarian Lev',
    'CZK': 'Czech Koruna',
    'DKK': 'Danish Krone',
    'GBP': 'British Pound Sterling',
    'HUF': 'Hungarian Forint',
    'PLN': 'Polish Złoty',
    'RON': 'Romanian Leu',
    'SEK': 'Swedish Krona',
    'CHF': 'Swiss Franc',
    'ISK': 'Icelandic Króna',
    'NOK': 'Norwegian Krone',
    'TRY': 'Turkish Lira',
    'AUD': 'Australian Dollar',
    'BRL': 'Brazilian Real',
    'CAD': 'Canadian Dollar',
    'CNY': 'Chinese Yuan Renminbi',
    'HKD': 'Hong Kong Dollar',
    'IDR': 'Indonesian Rupiah',
    'INR': 'Indian Rupee',
    'KRW': 'South Korean Won',
    'MXN': 'Mexican Peso',
    'MYR': 'Malaysian Ringgit',
    'NZD': 'New Zealand Dollar',
    'PHP': 'Philippine Peso',
    'SGD': 'Singapore Dollar',
    'THB': 'Thai Baht',
    'ZAR': 'South African Rand',
    'USD': 'United States Dollar'
}

# Create a small box in the sidebar and display the list of currencies
st.sidebar.markdown("### Currency Codes and Full Names:")
for code in currency_codes:
    st.sidebar.text(f"{code} - {currency_names.get(code, 'Unknown')}")


with st.form(key='currencyform'):
    box1,box2,box3=st.columns([3,2,2])
    with box1:
        amount=st.number_input('amount')
    with box2:
        From=st.selectbox('From',currency_codes,key='currency1')
    with box3:
        To=st.selectbox('To',currency_codes,key='currency2')
    submit=st.form_submit_button(label='convert')
if submit:
    a=round(c.convert(From,To,amount))
    output=(f':red[{amount}] {currency_names[From]}s is equal to :red[{a}] {currency_names[To]}s')
    st.info(output)
st.header('CURRENCY :red[RATES]')