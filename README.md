# Banco Digital  

O **Banco Digital** é uma plataforma bancária completa que oferece funcionalidades de gerenciamento de contas, transferências de dinheiro e pagamentos. O sistema é composto por um back-end robusto e seguro, além de um front-end moderno e intuitivo, projetado para oferecer a melhor experiência para os usuários.

## Funcionalidades  

1. **Cadastro de Usuários**:  
   - Nome completo, CPF/CNPJ, e-mail e senha.  
   - CPF/CNPJ e e-mails devem ser únicos no sistema.  
   - Dois tipos de usuários:  
     - **Clientes comuns**: podem realizar e receber transferências.  
     - **Lojistas**: apenas recebem transferências.  

2. **Transferências de Dinheiro**:  
   - Usuários comuns podem transferir dinheiro entre si ou para lojistas.  
   - Validação de saldo antes da transferência.  
   - Consulta a um serviço autorizador externo antes de confirmar a operação.  

3. **Transações Seguras**:  
   - Todas as transferências são tratadas como transações atômicas, garantindo que o dinheiro seja revertido em caso de inconsistências.  

4. **Notificações**:  
   - Ao receber pagamentos, o destinatário é notificado via e-mail.  
   - Integração com serviços externos para envio de notificações, incluindo tratamento de indisponibilidades.  

5. **APIs RESTful**:  
   - Implementação de endpoints seguindo boas práticas de design de APIs.  

---

## Requisitos  

Para o funcionamento do **Banco Digital**, as seguintes regras de negócio são implementadas:  

- O sistema não permite cadastros duplicados para o mesmo CPF/CNPJ ou e-mail.  
- Antes de concluir uma transferência:  
  - Validar se o saldo do pagador é suficiente.  
  - Consultar o serviço autorizador externo.  

---

## Endpoints  

