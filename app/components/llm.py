from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline
import torch

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def load_llm():
    try:
        logger.info("Loading Mistral-7B-Instruct-v0.3 on GPU...")

        model_id = "mistralai/Mistral-7B-Instruct-v0.3"

        tokenizer = AutoTokenizer.from_pretrained(model_id)

        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",          # 🔥 GPU auto placement
            torch_dtype=torch.float16,  # 🔥 GPU-friendly
            low_cpu_mem_usage=True
        )

        text_gen_pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=256,
            temperature=0.3,
            return_full_text=False
        )

        llm = HuggingFacePipeline(pipeline=text_gen_pipeline)

        logger.info("LLM loaded successfully on GPU.")
        return llm

    except Exception as e:
        logger.error("Error while loading LLM", exc_info=True)
        raise CustomException("Failed to load Mistral LLM on GPU", e)
