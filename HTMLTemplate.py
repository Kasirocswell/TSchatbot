css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2f2b3e
}
.chat-message.bot {
    background-color: #6d7b99
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%; /* Ensure the avatar is a perfect circle */
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/GxFxZjj/image1.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7NNP7ZAelPQdieBT_6drWwyPZZmtS9Q0-oA&usqp=CAU">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
