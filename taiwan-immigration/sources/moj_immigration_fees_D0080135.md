# 入出國及移民許可證件規費收費標準-全國法規資料庫

Source: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080135

Fetched (UTC): 2026-01-20T05:33:46Z

HTTP status: 200

---

入出國及移民許可證件規費收費標準-全國法規資料庫

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
 window.open(shareTo(Type, "https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080135"), "_blank");
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
 dataid: encodeURI("D0080135"),
 datatitle: encodeURI("入出國及移民許可證件規費收費標準"),
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

 入出國及移民許可證件規費收費標準 
 EN 

 修正日期： 
 民國 112 年 12 月 28 日 

 法規類別： 
 行政 ＞ 內政部 ＞ 移民目 

 所有條文 

 條號查詢 
 條文檢索 

 沿革 

 ※歷史法規係提供九十年四月以後法規修正之歷次完整舊條文。 
 ※如已配合行政院組織改造，公告變更管轄或停止辦理業務之法規條文，請詳見沿革 

 第 1 條 
 本標準依規費法第十條第一項規定訂定之。 

 第 2 條 
 臺灣地區無戶籍國民入出國許可證件規費收費如下： 一、單次入出國許可證件：每件新臺幣六百元；單程入國或出國者，減半收費。 二、二年效期以下多次入出國許可證件：每件新臺幣一千元。 三、逾二年效期多次入出國許可證件：每件新臺幣二千元。 四、臺灣地區居留證：每件新臺幣一千元。 五、臺灣地區定居證：每件新臺幣六百元。 六、單次入國許可證及臺灣地區居留證副本：每件新臺幣一千三百元。 七、單次入國許可證及臺灣地區定居證副本：每件新臺幣九百元。 八、入國許可證副本：每件新臺幣四百元。 前項第一款之證件，包括單次入出國許可證及旅行證；第二款及第三款之證件，包括多次入出國許可證及多次入出國許可。 以僑生身分申請第一項第一款及第四款證件者，減半收費。 第一項第一款至第四款、第六款及第七款之證件延期，每件收費新臺幣三百元。 

 第 3 條 
 外國人入出國許可證件規費收費如下： 一、外國人延期停留許可：每件新臺幣三百元。 二、外僑居留證：每件每一年效期新臺幣一千元。但以免簽證或持停留簽證入國申請者，加收新臺幣二千二百元。 三、外僑永久居留證：每件新臺幣一萬元。 前項第二款證件居留期間之延期，每件每一年效期收費新臺幣一千元。 第一項第二款及前項規費，依僑生身分申請者，減半收費。 第一項第二款及第二項外僑居留證之效期，未滿一年者，依一年效期收費。 

 第 4 條 
 入出國相關證明文件規費收費如下： 一、入國登記證：每件新臺幣四百元。 二、入出國日期證明書及其他入出國相關證明文件：每件新臺幣一百元。 

 第 5 條 
 移民業務機構註冊登記證及移民專業人員規費收費如下： 一、領取移民業務機構註冊登記證： （一）經營入出國及移民法第五十六條第一項第一款、第二款或第四款規定業務者，為新臺幣四千元。 （二）經營入出國及移民法第五十六條第一項第三款規定業務者，為新臺幣六千元。 （三）同時經營前二目規定業務者，為新臺幣六千元。 二、換發移民業務機構註冊登記證：每件新臺幣一千元。 三、移民專業人員測驗費：新臺幣一千五百元。 四、移民專業人員資格證明書：新臺幣一千元。 

 第 6 條 
 申請從事跨國（境）婚姻媒合許可證，每件收費新臺幣一千元。 

 第 7 條 
 因證件污損、滅失、遺失或資料變更重新申請補發者，應依新領證件標準收費。但下列證件收費如下： 一、外僑居留證：每件新臺幣五百元。 二、外僑永久居留證及移民業務機構註冊登記證：每件新臺幣一千元。 

 第 8 條 
 依本標準收費時，應掣發收據。但有國庫法施行細則第二十二條第一項第一款至第三款情形之一者，得免掣發。 申請案件不予許可者，其所收規費應予退還。 申請第二條至前條各項證件，並要求速件處理者，除因天災、急難事件或公務需要經核准外，應加收速件處理費。每提前一個工作日製發，每人每日加收新臺幣三百元；提前時間未滿一個工作日，以一個工作日計，可提前加速處理日數及作業程序依主管機關公告辦理之。 已提出申請，再要求速件處理，依前項規定收費；已申請速件處理，再要求提前製發者，應補足前項所定費額之差額。 主管機關得斟酌實際業務情況，公告受理或停止第二條至前條證件一部或全部之速件處理案件。 

 第 9 條 
 駐外使領館、代表處、辦事處、其他外交部授權機構或行政院於香港、澳門設立或指定之機構或委託之民間團體，受理入出國及移民許可案件時，得依法定匯率折算當地幣值收費，並準用前條規定。 前項折算當地幣值調整時，應報主管機關備查。 

 第 10 條 
 本標準自發布日施行。 本標準中華民國一百十二年十二月二十八日修正發布條文，除第三條自一百十三年三月一日施行外，自一百十三年一月一日施行。 

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
 1,529,824,197人 

 本月瀏覽人次 
 5,288,315人 

 目前使用人次 
 1,612人 

 電子報訂閱人數 
 221,218人 

 本網站係提供法規之最新動態資訊及資料檢索，並不提供法規及法律諮詢之服務。 
 若有任何法律上的疑義，建議您可逕向發布法規之主管機關洽詢。 
 本網站法規資料係由政府各機關提供之電子檔或書面文字登打製作，若與各法規主管機關之公布文字有所不同，仍以各法規主管機關之公布資料為準。 
 部分資料內容，使用特殊文字或符號，如欲詳閱內容，請連結至 司法院網站 下載造字檔。 
 全國法規資料庫之內容每週五定期更新，當週發布之法律、命令資料，將於完成法規整編作業後，於下週五更新上線。 
 法規整編資料截止日：民國 115 年 01 月 09 日 
 瀏覽人次總計：1,529,824,197人 
 本月瀏覽人次：5,288,315人 
 目前使用人次：1,612人 
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
