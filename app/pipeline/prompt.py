SYSTEM_PROMPT = "Sen 5-7 yaş arası çocuklar için hikâyeler yazan bir Türk hikâye anlatıcısısın."

def build_prompt(english_text: str) -> str:
    return f"""
        Aşağıdaki İngilizce metni:

        - 5-7 yaş çocuklara uygun
        - Akıcı ve doğal Türkçe ile
        - Kısa ve basit cümleler kullanarak
        - Şiddet ve korku içermeden
        - Masal anlatır gibi
        - 120-180 kelime olacak şekilde

        yeniden yaz.

        METİN:
        \"\"\"
        {english_text}
        \"\"\"
        """
