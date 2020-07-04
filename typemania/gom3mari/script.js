var _data = JSON.parse(`{"lyrics":[{"line":"","time":-1},{"line":"곰 세마리가 한 집에 있어","note":"Verse 1","time":3200},{"line":"아빠곰 엄마곰 애기곰","time":6800},{"line":"아빠곰은 뚱뚱해","time":10000},{"line":"엄마곰은 날씬해","time":13500},{"line":"애기곰은 너무 귀여워","time":17000},{"line":"으쓱으쓱 잘한다","time":20500}]}`);
var _types = JSON.parse(`{"types":[
  {"72":true,"82":true,"s":3300,"e":3900,"c":"곰"},
  {"80":true,"84":true,"s":3900,"e":4200,"c":"세"},
  {"65":true,"75":true,"s":4200,"e":4500,"c":"마"},
  {"70":true,"76":true,"s":4500,"e":4850,"c":"리"},
  {"75":true,"82":true,"s":4850,"e":5300,"c":"가"},
  {"71":true,"75":true,"s":5350,"e":5700,"c":"한"},
  {"76":true,"87":true,"s":5700,"e":6000,"c":"집"},
  {"68":true,"80":true,"s":6000,"e":6300,"c":"에"},
  {"68":true,"76":true,"s":6300,"e":6550,"c":"있"},
  {"68":true,"74":true,"s":6550,"e":6800,"c":"어"},
  {"68":true,"75":true,"s":6800,"e":7200,"c":"아"},
  {"16":true,"75":true,"81":true,"s":7200,"e":7500,"c":"빠"},
  {"72":true,"82":true,"s":7500,"e":7800,"c":"곰"},
  {"68":true,"74":true,"s":7800,"e":8200,"c":"엄"},
  {"65":true,"75":true,"s":8200,"e":8500,"c":"마"},
  {"72":true,"82":true,"s":8500,"e":8800,"c":"곰"},
  {"68":true,"79":true,"s":8800,"e":9200,"c":"애"},
  {"76":true,"82":true,"s":9200,"e":9600,"c":"기"},
  {"72":true,"82":true,"s":9600,"e":10000,"c":"곰"},
  {"68":true,"75":true,"s":10500,"e":10850,"c":"아"},
  {"16":true,"75":true,"81":true,"s":10850,"e":11250,"c":"빠"},
  {"72":true,"82":true,"s":11250,"e":11750,"c":"곰"},
  {"68":true,"77":true,"s":11750,"e":12100,"c":"은"},
  {"16":true,"69":true,"78":true,"s":12100,"e":12500,"c":"뚱"},
  {"16":true,"69":true,"78":true,"s":12500,"e":13000,"c":"뚱"},
  {"71":true,"79":true,"s":13000,"e":13600,"c":"해"},
  {"68":true,"74":true,"s":13900,"e":14300,"c":"엄"},
  {"65":true,"75":true,"s":14300,"e":14800,"c":"마"},
  {"72":true,"82":true,"s":14800,"e":15300,"c":"곰"},
  {"68":true,"77":true,"s":15300,"e":15700,"c":"은"},
  {"75":true,"83":true,"s":15700,"e":16100,"c":"날"},
  {"16":true,"76":true,"84":true,"s":16100,"e":16550,"c":"씬"},
  {"71":true,"79":true,"s":16550,"e":17000,"c":"해"},
  {"68":true,"79":true,"s":17300,"e":17800,"c":"애"},
  {"76":true,"82":true,"s":17800,"e":18200,"c":"기"},
  {"72":true,"82":true,"s":18200,"e":18700,"c":"곰"},
  {"68":true,"77":true,"s":18700,"e":19050,"c":"은"},
  {"74":true,"83":true,"s":19050,"e":19300,"c":"너"},
  {"65":true,"78":true,"s":19300,"e":19550,"c":"무"},
  {"76":true,"78":true,"82":true,"s":19550,"e":19800,"c":"귀"},
  {"68":true,"85":true,"s":19800,"e":20000,"c":"여"},
  {"68":true,"74":true,"78":true,"s":20000,"e":20500,"c":"워"},
  {"68":true,"77":true,"s":20800,"e":21200,"c":"으"},
  {"16":true,"77":true,"84":true,"s":21200,"e":21600,"c":"쓱"},
  {"68":true,"77":true,"s":21600,"e":22000,"c":"으"},
  {"16":true,"77":true,"84":true,"s":22000,"e":22400,"c":"쓱"},
  {"75":true,"87":true,"s":22400,"e":22900,"c":"잘"},
  {"71":true,"75":true,"s":22900,"e":23400,"c":"한"},
  {"69":true,"75":true,"s":23400,"e":24400,"c":"다"}
]}`);

var currentLine = "";
//var combo = 0;
var score = 0;

function align() {
   var a = $(".highlighted").height();
   var c = $(".content").height();
   var d = $(".highlighted").offset().top - $(".highlighted").parent().offset().top;
   var e = d + (a/2) - (c/2);
   $(".content").animate(
       {scrollTop: e + "px"}, {easing: "swing", duration: 250}
   );
}

var lyricHeight = $(".lyrics").height();
$(window).on("resize", function() {
   if ($(".lyrics").height() != lyricHeight) { //Either width changes so that a line may take up or use less vertical space or the window height changes, 2 in 1
      lyricHeight = $(".lyrics").height();
      align();
   }
});

var vid = document.getElementById("myVideo");
function enableAutoplay() {
  $("button").css("display","none");
  vid.autoplay = true;
  vid.load();
}
var curtime = 0;

function check_score(time) {
  var past2 = _types["types"].filter(function (item) {
    return item.s < time;
  });

  if (past2.length > 0 && time >= _types["types"][past2.length-1].s && time <= _types["types"][past2.length-1].e){
    //console.log("cur_time",past2.length, time);
    var cur_types = $.extend(true, {}, _types["types"][past2.length-1])
    delete cur_types.s;
    delete cur_types.e;
    delete cur_types.c;
    var ks = Object.keys(keys);
    var cur_types_ks = Object.keys(cur_types);
    ks.forEach(function(key){
      if(key in cur_types){
        score += 100;
      }
    });
  }
}

var keys = {};
$(document).ready(function(){
   $("video").on('timeupdate', function(e){
      var time = this.currentTime*1000;
      curtime = time;
      var past = _data["lyrics"].filter(function (item) {
         return item.time < time;
      });
      if (_data["lyrics"][past.length] != currentLine) {
         currentLine = _data["lyrics"][past.length];
         $(".lyrics div").removeClass("highlighted");
         $(`.lyrics div:nth-child(${past.length})`).addClass("highlighted"); //Text might take up more lines, do before realigning
         align();
      }
      $("#keys").html(score);
   });
});

$(document).keydown(function (e) {
    keys[e.which.toString()] = true;
    curtime = document.getElementById("myVideo").currentTime * 1000;
    check_score(curtime);
    //$("#keys").html(JSON.stringify(keys) + ", score:" + score);
    $("#keys").html(score);
});
$(document).keyup(function (e) {
    setTimeout(function(){
      delete keys[e.which.toString()];
    }, 300);
    //$("#keys").html(JSON.stringify(keys) + ", score:" + score);
    $("#keys").html(score);
});

generate();

function generate() {
   var html = "";
   for(var i = 0; i < _data["lyrics"].length; i++) {
      html += "<div";
      if(i == 0) {
         html+=` class="highlighted"`;
         currentLine = 0;
      }
      if(_data["lyrics"][i]["note"]) {
         html += ` note="${_data["lyrics"][i]["note"]}"`;
      }
      html += ">";
      html += _data["lyrics"][i]["line"] == "" ? "•" : _data["lyrics"][i]["line"];
      html += "</div>"
   }
   $(".lyrics").html(html);
   align();
}
