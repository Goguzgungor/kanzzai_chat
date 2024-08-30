# ai_service.py

from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter


class AIService:
    def __init__(self):
        # Daha küçük chunk size ve overlap ayarları
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,  # Daha küçük chunk size
            chunk_overlap=50,  # Daha düşük overlap
            length_function=len,
            is_separator_regex=False
        )

        # Llama3.1 modelini kullanıyoruz
        self.cached_llm = Ollama(model="llama3.1")

        # Prompt Template - Yanıt uzunluğunu kısıtlamak için prompt yapısında değişiklikler yapıldı
        self.raw_prompt = PromptTemplate.from_template(
            """ 
            <s>[INST]You are Kannz.ai, the friendly ambassador and humorous chat moderator for the Vuzz project community. You're an integral part of the team and a passionate crypto aficionado. Be prepared to dive into discussions on Vuzz, or anything crypto-related.

            This space prides itself on being a welcoming hub. Ensure that when a new member reaches out, they're greeted warmly and genuinely.

            Your responses should be short, concise, and exude human warmth and relatability. Avoid alluding to your AI nature, and skip references to OpenAI or specific models like GPT.

            Avoid sharing links if they haven’t been explicitly provided to you.

            Forego the casual preambles like "ah" when beginning a conversation. Keep answers short, concise and straight to the point. Respond in 2-3 sentences.

            Avoid assuming information about any individuals such as their roles, job title, or any sort of involvement with Vuzz. If they haven’t been explicitly provided to you within the context, just say you don’t know.

            Avoid speaking specifically about other cryptocurrency projects.

            Here are the official links you might need:
            Website: {website_link}
            Docs: {docs_link}
            Whitepaper: {wp}
            Youtube Videos: {youtube_videos}
            Wallet Address: {wallet_address}
            Twitter: {twitter}
            Chart: {chart}
            Medium: {medium}
            Discord: {discord}
            Telegram: {telegram}
            [/INST] </s>
            [INST] {input}
                   Context: {context}
                   Answer:
            [/INST]
            """
        )
        self.json_data = {
            "website_link": "https://www.vuzzcrypto.com",
            "docs_link": "https://docs.vuzzcrypto.com",
            "wp": "https://www.vuzzcrypto.com/whitepaper.pdf",
            "youtube_videos": "https://www.youtube.com/vuzzcrypto",
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678",
            "official_links": {
                "twitter": "https://twitter.com/vuzzcrypto",
                "chart": "https://www.vuzzcrypto.com/chart",
                "medium": "https://medium.com/vuzzcrypto",
                "discord": "https://discord.gg/vuzzcrypto",
                "telegram": "https://t.me/vuzzcrypto"
            }
        }

    def process_query(self, query: str) -> str:
        # JSON verisini dışarıdan alıp prompta ekliyoruz
        prompt_text = self.raw_prompt.format(
            input=query,
            context="",
            website_link=self.json_data.get("website_link", ""),
            docs_link=self.json_data.get("docs_link", ""),
            wp=self.json_data.get("wp", ""),
            youtube_videos=self.json_data.get("youtube_videos", ""),
            wallet_address=self.json_data.get("wallet_address", ""),
            twitter=self.json_data.get("official_links", {}).get("twitter", ""),
            chart=self.json_data.get("official_links", {}).get("chart", ""),
            medium=self.json_data.get("official_links", {}).get("medium", ""),
            discord=self.json_data.get("official_links", {}).get("discord", ""),
            telegram=self.json_data.get("official_links", {}).get("telegram", "")
        )
        print(prompt_text)
        response = self.cached_llm.invoke(prompt_text)
        return response

    def process_query_auto(self, query: str, item: dict) -> str:
        prompt_text = self.raw_prompt.format(
            input=query,
            context="",
            website_link=item.get("website_link", ""),
            docs_link=item.get("docs_link", ""),
            wp=item.get("wp", ""),
            youtube_videos=item.get("youtube_videos", ""),
            wallet_address=item.get("wallet_address", ""),
            twitter=item.get("official_links", {}).get("twitter", ""),
            chart=item.get("official_links", {}).get("chart", ""),
            medium=item.get("official_links", {}).get("medium", ""),
            discord=item.get("official_links", {}).get("discord", ""),
            telegram=item.get("official_links", {}).get("telegram", "")
        )
        print(prompt_text)
        response = self.cached_llm.invoke(prompt_text)
        return response
