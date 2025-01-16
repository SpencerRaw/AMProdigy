from fastapi import FastAPI
from pydantic import BaseModel
import peptides

# 定义请求模型
class PeptideRequest(BaseModel):
    sequence: str

# 定义 FastAPI 应用
app = FastAPI()



def calculate_descriptors(peptide_sequence: str):
    # 创建一个 Peptide 对象
    peptide = peptides.Peptide(peptide_sequence)
    
    # 调用 descriptors 方法计算物理化学属性
    descriptors = peptide.descriptors()
    
    # 返回结果
    return descriptors


# 定义一个 POST 端点
@app.post("/calculate_descriptors/")
def calculate_peptide_descriptors(request: PeptideRequest):
    result = calculate_descriptors(request.sequence)
    return result

