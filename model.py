import torch
import torch.nn as nn
from transformers import BertModel

class BiLSTMClassifier(nn.Module):
    def __init__(self, num_tactics, num_techniques):
        super(BiLSTMClassifier, self).__init__()
        self.bert = BertModel.from_pretrained('allenai/scibert_scivocab_uncased', local_files_only=True)
        self.lstm = nn.LSTM(768, 256, batch_first=True, bidirectional=True)
        self.drop = nn.Dropout(0.3)
        self.fc_tactic = nn.Linear(512, num_tactics)
        self.fc_technique = nn.Linear(512, num_techniques)

    def forward(self, input_ids, attention_mask):
        with torch.no_grad():
            outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        sequence_output = outputs.last_hidden_state
        lstm_out, _ = self.lstm(sequence_output)
        out = self.drop(lstm_out[:, -1, :])
        tactic_logits = self.fc_tactic(out)
        technique_logits = self.fc_technique(out)
        return tactic_logits, technique_logits
