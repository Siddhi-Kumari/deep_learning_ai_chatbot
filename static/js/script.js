$(document).ready(function(){
    $('#send_btn').click(function(){
        let userMessage = $('#user_input').val();
        
        if(userMessage.trim() === '') return;

        // Display the user's message in chat
        $('#chatlogs').append('<div class="user-msg">You: ' + userMessage + '</div>');
        
        // Scroll to the bottom of the chatlogs
        $('#chatlogs').scrollTop($('#chatlogs')[0].scrollHeight);

        // Display typing animation before the bot's response
        $('#chatlogs').append('<div class="bot-msg typing">Bot is typing...</div>');

        // Send the message to the backend
        $.ajax({
            url: '/handle_message',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ "message": userMessage }),
            success: function(response){
                let botResponse = response.response;
                
                // Remove typing animation and display the bot's response
                setTimeout(function() {
                    $('.typing').remove();
                    $('#chatlogs').append('<div class="bot-msg">Bot: ' + botResponse + '</div>');
                    $('#chatlogs').scrollTop($('#chatlogs')[0].scrollHeight);
                }, 1500); // Adjust timing to your liking
                
                // Clear the input field
                $('#user_input').val('');
            },
            error: function(error) {
                console.error("Error:", error);
                $('#chatlogs').append('<div class="bot-msg">Bot: Oops! Something went wrong.</div>');
                $('#chatlogs').scrollTop($('#chatlogs')[0].scrollHeight);
            }
        });
    });

    // Optional: Press Enter to send message
    $('#user_input').keypress(function(e) {
        if (e.which == 13) {
            $('#send_btn').click();
        }
    });
});
