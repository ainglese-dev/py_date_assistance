# List of Latin American country codes excluding Brazil
latam_country_codes = [
    'AR',  # Argentina
    'CL',  # Chile
    'CO',  # Colombia
    'CR',  # Costa Rica
    'DO',  # Dominican Republic
    'EC',  # Ecuador
    'SV',  # El Salvador
    'GT',  # Guatemala
    'HN',  # Honduras
    'MX',  # Mexico
    'PA',  # Panama
    'PY',  # Paraguay
    'PE',  # Peru
    'PR',  # Puerto Rico
    'UY',  # Uruguay
    'VE'   # Venezuela
]

# Dictionary to map country codes to flag emojis
country_flags = {
    'AR': '🇦🇷', 'CL': '🇨🇱', 'CO': '🇨🇴', 'CR': '🇨🇷', 'DO': '🇩🇴',
    'EC': '🇪🇨', 'SV': '🇸🇻', 'GT': '🇬🇹', 'HN': '🇭🇳', 'MX': '🇲🇽',
    'PA': '🇵🇦', 'PY': '🇵🇾', 'PE': '🇵🇪', 'PR': '🇵🇷', 'UY': '🇺🇾',
    'VE': '🇻🇪'
}

country_timezones_to_exclude = {
    'EC': ['America/Guayaquil'],  # Include only Quito timezone for Ecuador
    'MX': ['America/Mexico_City'],  # Include only Mexico City timezone for Mexico
    'CL': ['America/Santiago']  # Include only Santiago timezone for Chile
}