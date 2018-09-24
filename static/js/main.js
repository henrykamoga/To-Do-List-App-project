
document.addEventListener('DOMContentLoaded', function ()
{
var typed = new Typed(".type-wrap", {
			  stringsElement: '#type_my_strings',
			  typeSpeed: 95, //100
			  backSpeed: 0,
			  loop:true,
			  backDelay:3500,
			// loopCount: Infinity,
			  //startDelay:1000,

			  //shuffle: false,
			  fadeOut: false,
			  fadeOutClass: 'typed-fade-out',
			  fadeOutDelay: 500,
			  onStop: function (pos, self) {prettyLog('onStop ' + pos + ' ' + self) },
			  onStart: function(pos, self) { prettyLog('onStart ' + pos + ' ' + self) },
			  onRestart: function (self) {prettyLog('onReset ' + self) },
			  

			  
			});
			document.querySelector('.resume_pause').addEventListener('click', function () {
				typed.toggle();
			});
			
			document.querySelector('.restart').addEventListener('click', function (){
				typed.reset();
			});
			document.querySelector('.start').addEventListener('click', function (){
				typed.start();
			});

			/*tYPING MULTIPLE LINES */

}); /* for addEventListener */


function prettyLog(str) {
  console.log('%c ' + str, 'color: green; font-weight: bold;');
}


function Change_color () 
	{
		var change_me = document.getElementById("Terminal_Streaming_Div")
		change_me.style.backgroundColor = ((change_me.style.backgroundColor == "red") ? "#7FFF00" : "red")
	};
setInterval(Change_color,300);