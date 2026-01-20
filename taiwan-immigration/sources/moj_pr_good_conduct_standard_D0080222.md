# 外國人申請永久居留無不良素行認定標準-全國法規資料庫

Source: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080222

Fetched (UTC): 2026-01-20T05:33:46Z

HTTP status: 200

---

外國人申請永久居留無不良素行認定標準-全國法規資料庫

 .line-0000 {margin-left: 1em; text-indent: -0em;}
.line-0004 {margin-left: 3em; text-indent: -2em;}
.line-0006 {margin-left: 4em; text-indent: -3em;}

 try {
 if (top.location.host != window.location.host)
 top.location = window.location;
 }
 catch (err) {
 top.location = window.location;
 }

 window.dataLayer = window.dataLayer || [];
 function gtag() { dataLayer.push(arguments); }
 gtag('js', new Date());
 gtag('config', 'G-QFLS1G3FEY', { cookie_flags: 'max-age=7200;SameSite=Strict;Secure' });

 您的瀏覽器，不支援javascript script語法，恐影響到網頁的閱讀 

 跳至主要內容 

 ::: 
 網站導覽 
 English 
 會員登入 

 小字型 
 中字型 
 大字型 

 整合查詢 

 整合查詢 
 最新訊息 
 中央法規 
 司法解釋 
 條約協定 
 兩岸協議 
 智慧查找 

 熱門詞彙： 刑法 、 職業安全衛生 、 勞基法 、 憲法 、 採購法 

 最新訊息 
 中央法規 
 司法解釋 
 條約協定 
 兩岸協議 
 綜合查詢 
 跨機關檢索 

 熱門法規 
 相關連結 
 網站導覽 
 English 
 會員登入 

 ::: 

 現在位置：
 首頁 
 中央法規 
 所有條文 

 P 

 $(function () {
 $(".share-bar").css("display", "inline-block");
 $(".share-bar a").on("click keypress ", function (event) {
 if (event.keyCode == 13 || event.button == 0) {
 event.preventDefault();
 var Type = $(this).data("sharetype");
 if (Type != "PDF")
 window.open(shareTo(Type, "https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080222"), "_blank");
 else window.location.href = $('#hlkPdf').attr("href");
 }
 });
 });

 下載 
 友善列印 

 加入資料夾： 

 儲存 

 確定 
 新增資料夾 
 管理資料夾 

 $(function () {
 //無障礙，預設隱藏，JS有啟用時才看的到
 $("#hlAddToFolder").removeClass("hidden");
 $(".folder-menu li").last().hide();
 $("#hlNewFolder").on("click", function (event) {
 event.preventDefault();
 $(".folder-menu li").last().toggle();
 if ($(this).text() == "新增資料夾") {
 $("#txtNewFolder").focus();
 $(this).text("取消");
 }
 else
 $(this).text("新增資料夾");
 });
 $("#btnAddNewFolder").on("click", function (event) {
 var fname = $.trim($("#txtNewFolder").val());
 if (fname == "") return false;

 $.ajax({
 url: "../controls/FolderHandler.ashx",
 type: "POST",
 dataType: "json",
 data: {
 foldername: encodeURI($.trim($("#txtNewFolder").val()))
 },
 success: function (data) {

 $.each(data, function (index, element) {
 $(" " + element.NAME + " ")
 .insertBefore($("#folderlist li:last"));
 $("#txtNewFolder").val("");
 $(".folder-menu li").last().hide();
 });
 }
 });
 });
 $("#hlSaveToFolder").on("click", function (event) {
 var checkedFID = $("#folderlist input[type='checkbox']:checked").map(function () { return this.value; }).get().join(',');
 if (checkedFID == "") {
 alert("請選擇所要儲存的資料夾。")
 return false;
 }
 $.ajax({
 url: "../controls/FolderHandler.ashx",
 type: "POST",
 data: {
 lan: "C",
 datatype: encodeURI("01"),
 dataid: encodeURI("D0080222"),
 datatitle: encodeURI("外國人申請永久居留無不良素行認定標準"),
 fid: encodeURI(checkedFID)
 },
 success: function (data) {
 alert("您已成功儲存此頁至您個人資料夾。");
 $("#folderlist input[type='checkbox']").prop("checked", false);
 $("#folderlist").collapse("hide");
 }
 });
 });
 $('#hlMoveToFolder').on("click", function () {
 var x = $('#hfSelect').val();
 var checkedFID = $("#folderlist input[type='checkbox']:checked").map(function () { return this.value; }).get().join(',');
 if (checkedFID == "") {
 alert("請選擇所要儲存的資料夾。")
 return false;
 }
 if (x=='') {
 alert("請選擇所要搬移的資料。")
 return false;
 }
 $.ajax({
 url: "../controls/FolderMoveHandler.ashx",
 type: "POST",
 data: {
 rfid: encodeURI(''),
 did: encodeURI(x),
 fid: encodeURI(checkedFID)
 },
 success: function (data) {
 alert("您已成功儲存此頁至您個人資料夾。");
 $("#folderlist input[type='checkbox']").prop("checked", false);
 $("#folderlist").collapse("hide");
 window.location.reload();
 }
 });
 });
 });

 所有條文 

 法規名稱： 

 外國人申請永久居留無不良素行認定標準 
 EN 

 發布日期： 
 民國 112 年 12 月 27 日 

 法規類別： 
 行政 ＞ 內政部 ＞ 移民目 

 所有條文 

 條號查詢 
 條文檢索 

 沿革 

 ※歷史法規係提供九十年四月以後法規修正之歷次完整舊條文。 
 ※如已配合行政院組織改造，公告變更管轄或停止辦理業務之法規條文，請詳見沿革 

 第 1 條 
 本標準依入出國及移民法（以下簡稱本法）第二十五條第十二項規定訂定之。 

 第 2 條 
 本法第二十五條第一項第二款所稱不良素行，指有下列情形之一者： 一、因犯罪受緩起訴處分或拘役、罰金、緩刑判決確定。但因過失犯罪者，不在此限。 二、違反下列社會秩序維護法行為之一，經裁處拘留或罰鍰確定尚未執行或繳納完畢： （一）無正當理由攜帶具有殺傷力之器械、化學製劑或其他危險物品。 （二）放置、投擲或發射有殺傷力之物品而有危害他人身體或財物之虞。 （三）主持、操縱或參加不良組織有危害社會秩序。 （四）吸食或施打煙毒或麻醉藥品以外之迷幻物品。 （五）在公共場所或公眾得出入之場所，意圖與人性交易或媒合性交易而拉客。 （六）非依自治條例規定，媒合或從事性交易。 （七）意圖鬥毆而聚眾。 三、對其具有中華民國國籍之配偶或未成年子女未盡法定扶養義務，經法院判決確定；或有事實足認無正當理由未盡該法定扶養義務。 四、對其具有中華民國國籍之親屬有習慣性家庭暴力行為，經法院判決確定。 五、有事實足認對其具有中華民國國籍之親屬有習慣性家庭暴力行為。但其情可憫、係出於自我防衛或不可歸責於申請人者，不在此限。 六、在我國居留期間曾對兒童及少年有性侵害、性剝削、性霸凌、性騷擾或跟蹤騷擾等行為，或違反兒童及少年福利與權益保障法第四十九條第一項規定，經有關機關查證屬實。 

 第 3 條 
 有下列情形之一者，得認定無不良素行： 一、緩起訴處分或緩刑期滿未經撤銷。 二、罰金執行完畢。 三、拘役執行完畢逾三年。 四、犯最重本刑為六月以下有期徒刑、拘役或罰金之罪，其行刑權時效完成逾三年。 五、依前條第二款處罰經執行或繳納完畢或執行時效屆滿；或有前條第二款第五目或第六目行為，其情可憫或不可歸責於申請人。 六、前條第三款至第五款之行為終了或完成後三年內，未再有前條所列行為。 七、前條第六款違法情事，罰鍰經繳納完畢、執行時效屆滿或依法免予處罰逾三年。 前條第六款行為構成犯罪，或故意對兒童及少年犯刑法傷害罪章之罪，受緩起訴處分、緩刑或罰金判決確定者，於前項第一款或第二款情形發生後逾三年，始得認定無不良素行。 

 第 4 條 
 內政部移民署就第二條第三款後段、第五款但書及前條第一項第五款後段所定有事實足認無正當理由、其情可憫、出於自我防衛或不可歸責於申請人之情形，應邀請專家學者及社會公正人士認定之。 

 第 5 條 
 第三條第一項第三款、第四款及第六款所定三年期間，於政府機關（構）、行政法人、社區或其他符合公益目的之機構或團體積極從事公益義務勞務二百四十小時以上，獲有證明者，得減為二年。 

 第 6 條 
 偵查或審判中之案件，應俟不起訴、緩起訴處分或判決確定後，再行認定有無不良素行。 

 第 7 條 
 本標準施行日期，由內政部定之。 

 ::: 

 最新訊息 
 中央法規 
 司法解釋 
 條約協定 
 兩岸協議 
 綜合查詢 
 跨機關檢索 

 法治宣導專區

 智慧查找 
 法律扶助 
 創意教案 

 法律時事漫談 

 網站使用說明

 網站使用手冊 
 會員服務介紹 
 網站單元簡介 
 法規資料檢索範圍 
 資料更新頻率說明 

 資訊服務

 全國法規連結圖示 
 全國法規作業要點 
 法規名稱英譯標準表 

 相關網站 

 訂閱電子報 

 瀏覽人次總計 
 1,529,824,220人 

 本月瀏覽人次 
 5,288,338人 

 目前使用人次 
 1,635人 

 電子報訂閱人數 
 221,218人 

 本網站係提供法規之最新動態資訊及資料檢索，並不提供法規及法律諮詢之服務。 
 若有任何法律上的疑義，建議您可逕向發布法規之主管機關洽詢。 
 本網站法規資料係由政府各機關提供之電子檔或書面文字登打製作，若與各法規主管機關之公布文字有所不同，仍以各法規主管機關之公布資料為準。 
 部分資料內容，使用特殊文字或符號，如欲詳閱內容，請連結至 司法院網站 下載造字檔。 
 全國法規資料庫之內容每週五定期更新，當週發布之法律、命令資料，將於完成法規整編作業後，於下週五更新上線。 
 法規整編資料截止日：民國 115 年 01 月 09 日 
 瀏覽人次總計：1,529,824,220人 
 本月瀏覽人次：5,288,338人 
 目前使用人次：1,635人 
 電子報訂閱：221,218人 

 │ 政府網站資料開放宣告 │ 隱私權保護宣告 │ 資訊安全政策 │ Q & A │ 意見回饋 │ API文件 │ 
 本網站由法務部全國法規資料庫工作小組維運管理.. 
 法務部地址：100204 台北市重慶南路一段130號 　 電話：(02)2191-0189 
 第二辦公室地址：100006 台北市貴陽街1段235號 　 電話：(02)2191-0189 

 回上方 

 $(function () {
 var b = 'ONEBAR';
 $("#btnSubscribe,#btnUnsubscribe").on("click", function (event) {
 //var email = $.trim($("#txtEMail").val());
 //if (email == "") {
 // event.preventDefault();
 // alert('請您輸入電子郵件地址。');
 // $("#txtEMail").focus();
 //}
 //else if (false == IsEMail(email)) {
 // event.preventDefault();
 // alert('請您輸入正確電子郵件地址。');
 // $("#txtEMail").focus();
 //}
 //else {
 // GoogleAnanlytice('中文', '訂閱電子報', '', '');
 //}
 var email = $.trim($("#txtEMail").val());
 //if (!validateEmail(email)) {
 // alert('請您輸入正確電子郵件地址。');
 // return false;
 //}

 });
 $('#btnQall').on("click", function () {
 if ($.trim($("#keyword").val()) == "") {
 alert("請輸入關鍵字"); return false;
 }
 else {
 GoogleAnanlytice("中文", "整合查詢-首頁", "", "");
 return true;
 }
 });
 $('#btnDeepSearch').on("click", function () {
 var keyword = '';

 //20210315 加上判斷，取QueryString(KW)，若輸入關鍵字已搜尋過，則跳出提示訊息，避免重複搜尋
 Request = GetRequest();
 if ($.trim($("#keyword").val()) == "") {
 alert("請輸入關鍵字"); return false;
 }
 else if (keyword.indexOf($.trim($("#keyword").val())) >= 0) {
 alert("此關鍵字已包含至檢索字詞中，請重新輸入");
 return false;
 }
 else {
 GoogleAnanlytice("中文", "整合查詢-首頁", "", "");
 return true;
 }
 });
 $('#btnMsQall').on("click", function () {
 if ($.trim($("#msKeyword").val()) == "") {
 alert("請輸入關鍵字"); return false;
 } else {
 GoogleAnanlytice("中文", "整合查詢-首頁", "", "");
 return true;
 }
 });
 $('#btnMsDeepSearch').on("click", function () {
 var keyword = '';

 //20210315 加上判斷，取QueryString(KW)，若輸入關鍵字已搜尋過，則跳出提示訊息，避免重複搜尋
 Request = GetRequest();
 if ($.trim($("#msKeyword").val()) == "") {
 alert("請輸入關鍵字"); return false;
 } else if (keyword.indexOf($.trim($("#msKeyword").val())) >= 0) {
 alert("此關鍵字已包含至檢索字詞中，請重新輸入");
 return false;
 }
 else {
 GoogleAnanlytice("中文", "整合查詢-首頁", "", "");
 return true;
 }
 });
 //20210217 再檢索收合、展開功能
 $("#btnOpen").click(function () {
 if ($('#ulDeepSearch').css('overflow') == 'hidden') {
 $(this).html("收合");
 $(this).prop('title', '隱藏部分「再檢索」篩選條件，僅顯示一行');
 $("#ulDeepSearch").css("overflow", "inherit");
 }
 else {
 $(this).html("展開");
 $(this).prop('title', '顯示所有目前「再檢索」篩選條件');
 $("#ulDeepSearch").css("overflow", "hidden");
 }
 });
 $("#btnHelp").click(function () {
 OpenKeyWordHelp();
 return false;
 });
 $('#dropdownMenu').attr('data-bs-toggle', 'dropdown');
 $('#unitlist').on("click", "a", function (e) {
 e.preventDefault();
 var $this = $(this).parent();
 var a = $(this).html();
 b = $this.data("value");
 $this.addClass("select").siblings().removeClass("select");
 $("#dropdownMenu").html(a);
 $('#hidVal').val(b);
 });
 //$('#keyword').on('input propertychange paste keypress', function () {
 // BindAutocomplete('#keyword', b);
 //});
 BindAutocompletes('#keyword', b);
 function BindAutocompletes(orl, stype) {

 $(orl).autocomplete({
 source: function (request, response) {
 $.ajax({
 url: "../controls/GetTermList.ashx",
 type: 'post',
 dataType: "json",
 data: {
 term: request.term, type: stype
 },
 success: function (data) {
 response(data);
 }
 });
 },
 minLength: 1, //至少輸入幾個字元才開始給提示
 focus: function (event, ui) {
 return false;
 },
 select: function (event, ui) {
 if ($.trim(ui.item.PCODE).length == 0)
 $(this).val(ui.item.TERM);
 else
 location.href = "../Hot/AddHotLaw.ashx?pcode=" + encodeURIComponent(ui.item.PCODE);

 return false;
 },
 messages: { noResults: '', results: function () { } }//不顯示結果文字
 }).data("ui-autocomplete")._renderItem = function (ul, item) {
 if ($.trim(item.PCODE) != "")
 return $(" ")
 .append(" 直接連結 " + item.TERM + " ")
 .appendTo(ul);
 else {
 if (ul.find(".label-usual").length == 0)
 return $(" ")
 .append(" 常用詞彙 " + item.TERM + " ")
 .appendTo(ul);
 else
 return $(" ")
 .append(" " + item.TERM + " ")
 .appendTo(ul);
 }
 };
 }
 });
 function validateEmail(email) {
 if (email.includes("%")) {
 return false;
 }
 return true;
 }
 function OpenKeyWordHelp() {
 var a = "/Service/KeyWordHelp.html";
 TINY.box.show({ iframe: a, width: 810, height: 680 });
 //return false;
 }
 function GetRequest() {
 var url = location.search;
 var theRequest = new Object();
 if (url.indexOf("?") != -1) {
 var str = url.substr(1);
 strs = str.split("&");
 for (var i = 0; i 1200) {
 var Request = new Object();
 Request = GetRequest();
 var keyword = '';
 if (keyword != null && keyword.length > 26) {
 var ui = document.getElementById("btnOpen");
 ui.style.display = "";
 }
 } else {
 var Request = new Object();
 Request = GetRequest();
 var keyword = '';
 if (keyword != null && keyword.length > 19) {
 var ui = document.getElementById("btnOpen");
 ui.style.display = "";
 }
 }

 $(function () {
 $('[data-fancybox]').fancybox({
 toolbar: false,
 smallBtn: true,
 iframe: {
 css: {
 width: '400px',
 height: '170px'
 }
 }
 });
 });

//
