using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.WebSocket;


namespace finaldcbot
{
    class Program
    {
        private DiscordSocketClient _client;
        static void Main(string[] args)
         => new Program().MainAsync().GetAwaiter().GetResult();

            public async Task MainAsync()
            {
            _client = new DiscordSocketClient();

            _client.Log += Log;

            var token = "Njg1NjE1ODEzOTcyOTgzODc5.XmLPfA.8UP7wYtjl72ZthU31q3mjEwnMFw";


            await _client.LoginAsync(TokenType.Bot, token);
            await _client.StartAsync();

            await Task.Delay(-1);

            }
        
        private Task Log(LogMessage msg) 
        {
            
            Console.WriteLine(msg.ToString());
            return Task.CompletedTask;
        }
        
    }
}
