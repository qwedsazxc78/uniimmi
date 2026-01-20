# 外國人入出國境及居留停留規則-全國法規資料庫

Source: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080126

Fetched (UTC): 2026-01-20T05:33:46Z

HTTP status: 200

---

外國人入出國境及居留停留規則-全國法規資料庫

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
 window.open(shareTo(Type, "https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080126"), "_blank");
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
 dataid: encodeURI("D0080126"),
 datatitle: encodeURI("外國人入出國境及居留停留規則"),
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

 廢 
 外國人入出國境及居留停留規則 

 廢止日期： 
 民國 89 年 02 月 01 日 

 法規類別： 
 廢止法規 ＞ 內政部 

 所有條文 
 編章節 
 條號查詢 
 條文檢索 

 沿革 

 ※歷史法規係提供九十年四月以後法規修正之歷次完整舊條文。 
 ※如已配合行政院組織改造，公告變更管轄或停止辦理業務之法規條文，請詳見沿革 

 第 一 章 總則 
 第 1 條 外國人入出中華民國 (以下簡稱我國) 國境及在境內居留或停留，除條約
或法令另有規定外，依本規則之規定。 
 第 2 條 外國人在我國境內應隨身攜帶有效護照、外僑居留證或有關身分證明文件
。 
 第 二 章 入出國境 
 第 3 條 外國人在機場、港口入境時，應憑簽證隨整有效護照，並填寫入 (出) 境
登記表，經機場、港口警察機關查驗相符，加蓋入境驗訖戳記後，准許入
境。 
 第 4 條 外國人有下列情形之一者，得禁止其入境：
一、未帶有效護照或抗不繳驗者。
二、護照係偽造或變造者。
三、冒用或冒領他人護照者。
四、護照未經簽證或簽證失效者。
五、曾經拒絕入境、限令出境或驅逐出境者。
六、有妨害公共秩序或善良風俗之虞者。
七、有事實足認為精神病患，或經檢疫機關認有染疫或染疫之虞者。
八、攜帶違禁物品者。
九、有事實足認其在我國境內無力維持生活者。
十、持停留簽證而無回程或一目的地之機票、船票，或未辦妥次一目的地
 之入境簽證者。
十一、其行為有違反我國法令之虞者。
依前項規定被禁止人境之外國人，載運其來我國之航空器或船舶所屬之公
司或其代理人應負責以原班次或最近班次之航空器、船舶載運其離境。

 第 5 條 外國人有下列情形之一者，禁止其出境：
一、經司法機關通知限制出境者。
二、經財稅機關通知限制出境者。
外國人因其他案件在依法查證中，經有關機關請求限制出境者，得禁止其
出境。

 第 6 條 外國人在機場、港口出境時，應填繳出境登記表，連同護照，經查驗相符
加蓋出境驗訖戳記後，始得出境。 
 第 7 條 機長、船長或其所屬航空公司、輪船公司或其代理人於航空器、船舶到達
時或離境前，應向查驗單位提供下列資料：
一、進出機場、港口報告單。
二、旅客、航空器之機組員、空服人員或船員名單。
三、其他必要之資料。

 第 三 章 居留 
 第 8 條 外國人持居留簽證入境或入境後改發給居留簽證者，應自事實發生之日起
十五日內，向居留地警察局申請外僑居留證，逾期不申請者，限期於十日
內補辦，逾期不補辦者，限期離境。
外國人在我國境內出生，應由其父母或監護人於十五日內向居留地警察局
申請外僑居留證。
外僑居留證由內政部製備，由居留地警察局核發。 
 第 9 條 下列外國人，免辦外僑居留證：
一、駐我國使領館人員，經外交部發給外交官員證、領事官員證、使領館
 職員證或外籍隨從證者。
二、駐我國外國機構人員，經外交部發給外國機構官員證、職員證或外籍
 隨從證者。
三、駐我國國際機構人員，經外交部發給國際機構官員證、職員證或外籍
 隨從證者。
前項人員到任、調職、離任或遷移旅行之保護，由外交部通知內政部警政
署轉知相關警察機關辦理。

 第 10 條 下列外國人申請外僑居留證，其居留證有效期間依其居留原因定之。但最
長不得逾三年：
一、經依公司法核准認許之外國公司在我國境內負責人或其分公司經理人
 。
二、經目的事業主管機關依法核准在我國投資之外國投資人或外國法人投
 資人之代表人。
三、經目的事業主管機關依法核准受聘僱在我國工作或執業之外國人。

 第 11 條 下列外國人申請外僑居留證者，其居留證有效期間依其居留原因定之。但
最長不得逾一年：
一、經教育主管機關核准，在我國立 (備) 案之各級學校、國語文中心就
 學，或在學術、教育機關研究、指導或教學之人員。
二、經教育或其他有關主管機關核准，在我國立 (備) 案之各級學校選修
 或技藝單位學習之人員。
三、其他有居留需要之人員。

 第 12 條 外國人在我國依親生活，申請外僑居留證，得以其所依親屬之居留期間為
居留期間，其所依親屬為我國國民者，居留證有效期間最長不得逾三年。 
 第 13 條 外國人申請外僑居留證之手續如左：
一、填繳外僑居留證申請書一式三份。
二、繳附最近二吋半身脫帽正面照片四張。
三、繳驗護照及居留簽證。
四、檢附申請居留之證明文件。

 第 14 條 外國人居留期間屆滿而有繼續居留必要者，應於居留期滿前，申請延長居
留。
外國人於居留證有效期間內，居留原因消滅者，居留地警察局得註銷其居
留證，限期離境。 
 第 15 條 外國人居留原因變更者，應於十五日內向居留地警察局申請變更登記，並
重新核定其居留效期；逾期不申請者，限期於十日內補辦，逾期不補辦者
，限期離境。 
 第 16 條 外僑居留證遺失者，應向居留地警察局申請補發，其效期仍以原居留證之
效期為準。 
 第 17 條 外國人在居留地警察局管轄區域內變更居留住址者，應於十五日內持外僑
居留證向居留地警察局辦理住址變更登記；遷出居留地警察局管轄區域者
，應事前持外僑居留證向遷出地警察局辦理遷出登記，並於到達遷入地址
十五日內，向當地警察局辦理遷入登記。不依規定辦理登記者，經查明後
，得逕為登記。 
 第 18 條 有下列情形之一者，應自事實發生之日起三十日內，向居留地警察局申請
外僑居留證：
一、喪失我國國籍，尚未取得外國國籍者。
二、喪失外國國籍，尚未取得我國國籍者。
三、在我國境內出生，尚未取得外國國籍證明者。
前項第三款之情形，由其父母、親屬或兒童福利機構申請之。
依第一項規定申請外僑居留證者，準用第十三條第一款、第二款及第四款
規定。

 第 19 條 外國人在我國境內死亡，由其關係人或其本國駐華機構於十五日內，向居
留地警察局辦理外僑居留證註銷登記，或由居留地警察局查明後逕為登記
。
居留地警察局於辦理前項登記後，應即將登記事項通知其遺產稅主管稽徵
機關。 
 第 四 章 停留 
 第 20 條 外國人持停留簽證入境者，應於停留期限內離境。
外國人持可延長停留之簽證入境者，因故需延長停留時，應於停留期限屆
滿前向停留地警察局申請，每次延長不得逾原簽證許可停留之期限，以二
次為限。但合計停留期限不得逾六個月。
外國人停留限期屆滿，且不得延長者，如因不可抗力或其他重大事故必須
延長停留，應報由內政部警政署核准。 
 第 五 章 重入境許可 
 第 21 條 外國人於居留期間內有出境後再入境之必要者，應向居留地警察局申請核
發重入境許可。
前項重入境許可分為單次及多次使用二種，效期得與外僑居留證相同，外
僑居留證經註銷者，其重入境許可視同註銷。
第一項之重入境許可，得於申請外僑居留證時同時申請。 
 第 六 章 限令出境 
 第 22 條 外國人有下列情形之一，內政部得限令其出境：
一、經撤銷簽證者。
二、從事與原簽證目的不符之活動者。
三、犯罪經我國法院判決確定並執行完畢或經赦免者。
四、在我國境內無力維持生活者。
五、有妨害公共秩序或善良風俗之虞者。
六、犯罪經外國政府或國際組織請求協助查緝者。
七、其行為有違反我國法令之虞者。

 第 23 條 限令外國人出境之期限以七日以內為原則，逾期不出境者，得強制其出境
。限期離境者亦同。
外國人非法入境、逾期居留或逾期停留者，得逕行強制其出境。 
 第 24 條 外國人有下列各款情形之一者，得由當地警察局報請內政部警政署暫予收
容：
一、受驅逐出境之處分而尚未辦妥出境手續者。
二、非法入境、逾期居留或逾期停留者。
三、受限令出境之處分而有藏匿之虞或行為有違反我國法令之虞者。
四、其他有事實足認有暫予收容之必要者。
前項收容處所由內政部警政署設置之。

 第 七 章 附則 
 第 25 條 無國籍人入出我國國境及在境內居留或停留，準用本規則之規定。 
 第 26 條 外國人申請外僑居留證，應繳納證書費；其收費標準，由內政部定之。
前項證書費之收取，應循預算程序辦理。 
 第 27 條 外僑戶口查察實施規定由內政部警政署定之。 
 第 28 條 本規則自發布日施行。 

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
