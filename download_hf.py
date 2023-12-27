from huggingface_hub import snapshot_download
snapshot_download(repo_id = "SAGI-1/MultiModal_Mistral_Pretrain_V2", repo_type = "model", local_dir = "/workspace/BLIVA/pretrained_model")