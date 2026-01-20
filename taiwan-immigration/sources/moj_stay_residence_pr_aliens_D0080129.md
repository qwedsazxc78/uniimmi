# 外國人停留居留及永久居留辦法-全國法規資料庫

Source: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080129

Fetched (UTC): 2026-01-20T05:33:46Z

HTTP status: 200

---

外國人停留居留及永久居留辦法-全國法規資料庫

 .line-0000 {margin-left: 1em; text-indent: -0em;}
.line-0004 {margin-left: 3em; text-indent: -2em;}

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
 window.open(shareTo(Type, "https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080129"), "_blank");
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
 dataid: encodeURI("D0080129"),
 datatitle: encodeURI("外國人停留居留及永久居留辦法"),
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

 外國人停留居留及永久居留辦法 
 EN 

 修正日期： 
 民國 114 年 12 月 30 日 

 法規類別： 
 行政 ＞ 內政部 ＞ 移民目 

 所有條文 

 條號查詢 
 條文檢索 

 沿革 

 ※歷史法規係提供九十年四月以後法規修正之歷次完整舊條文。 
 ※如已配合行政院組織改造，公告變更管轄或停止辦理業務之法規條文，請詳見沿革 

 第 1 條 
 本辦法依入出國及移民法（以下簡稱本法）第三十五條規定訂定之。 

 第 2 條 
 外國人持停留簽證或以免簽證方式經查驗許可入國者，停留期間自入國之翌日起算，並應於停留期限屆滿前出國。 

 第 3 條 
 外國人依本法第三十一條第一項規定申請延期停留者，應於停留期限屆滿前十五日內，檢具下列文件及照片一張，向內政部移民署（以下簡稱移民署）申請： 一、申請書。 二、護照。 三、停留簽證。 四、其他相關證明文件。 依前項規定申請延期停留者，每次延期均不得逾原簽證許可停留之期間，其合計停留期間，並不得逾六個月。但有下列情形之一，並提出證明者，移民署得酌予再延長其停留期間： 一、懷胎七個月以上或生產、流產後二個月未滿。 二、罹患疾病住院或懷胎，搭機、船出國有生命危險之虞。 三、其配偶、直系血親、三親等內之旁系血親或二親等內之姻親在臺灣地區患重病或受重傷而住院需人照顧，或死亡須辦理喪葬事宜。 四、遭遇天災或其他不可避免之事變。 五、人身自由依法受拘束。 六、其子女在臺灣地區設有戶籍，且懷孕或育有二歲以下親生子女。 依前項各款規定之延長停留期間如下： 一、第一款或第二款：每次不得逾二個月。 二、第三款：自事由發生之日起，不得逾二個月。 三、第四款：不得逾一個月。 四、第五款：依事實需要核發。 五、第六款：不得逾六個月，以一次為限。 

 第 4 條 
 外國人以免簽證方式或抵我國時申請簽證，並經查驗許可入國，有外國護照簽證條例施行細則第四條各款情形之一，無法於停留期限屆滿前出國者，應向外交部領事事務局或其所屬分支機構申請停留簽證。 

 第 5 條 
 外國人持居留簽證經查驗許可入國後，應檢具下列文件及照片一張，向移民署申請居留，經許可者，核發外僑居留證： 一、申請書。 二、護照及居留簽證。 三、其他相關證明文件。 依本法第二十六條第一款至第三款規定申請居留者，免附前項第二款文件。 外國人於大陸地區出生，依第一項、第六條第一項或第十五條第一項規定申請居留或永久居留者，應另檢具其未在大陸地區設有戶籍及領用大陸地區護照之相關證明文件。 

 第 6 條 
 外國人依本法第二十三條規定申請居留者，應檢具下列文件及照片一張，向移民署申請，經許可者，核發外僑居留證： 一、申請書。 二、護照及停留簽證。但以免簽證方式經查驗許可入國者，免附停留簽證。 三、其他相關證明文件。 依前項規定申請居留，有本法第二十三條第一項第一款、第九款或第十款情形之一者，得自停留期限屆滿前三十日辦理；有本法第二十三條第一項第二款至第八款、第二項、第三項或第四項各款情形之一者，得自停留期限屆滿前十五日辦理。 依前項規定申請之外僑居留證，其有效期間自核發之翌日起算。 無國籍人民準用第一項規定申請居留者，移民署應會商相關機關審查。 

 第 7 條 
 外國人依本法第二十三條之一第一項規定申請變更居留原因者，應自事實發生之日起算三十日內，檢具下列文件及照片一張，向移民署申請，並重新核定居留期間： 一、申請書。 二、護照及外僑居留證。 三、其他相關證明文件。 外國人申請變更之居留原因非屬本法第二十三條之一第一項各款情形之一者，應自事實發生之日起算十五日內，向外交部領事事務局或其所屬分支機構重新申請居留簽證後，檢具前項各款文件、居留簽證及照片一張，向移民署申請居留。 

 第 8 條 
 本法中華民國八十八年五月二十一日施行前已入國之泰國、緬甸或印尼地區無國籍人民未能強制驅逐其出國者，向移民署申請居留，應檢具下列文件及照片一張，經許可者，核發外僑居留證： 一、申請書。 二、健康檢查合格證明。 三、起訴書或不起訴處分書。 四、出生地證明。 五、入國日期證明。 六、其他相關證明文件。 前項無國籍人民在臺灣地區出生之子女，得隨同申請居留。 依本條規定申請之外僑居留證，其有效期間自核發之翌日起算。 

 第 9 條 
 外國人依本法第三十一條第一項規定申請延期居留者，應於居留期限屆滿前三個月內，檢具下列文件及照片一張，向移民署申請： 一、申請書。 二、護照及外僑居留證。 三、其他相關證明文件。 外國人經許可在臺灣地區居留，年齡在十八歲以上，其父或母為現在在臺灣地區設有戶籍或經許可居留之我國國民、經許可居留或永久居留之外國人，或經許可居留之香港或澳門居民，且有下列情形之一者，得申請延期居留： 一、曾在我國合法累計居留十年，每年居住二百七十日以上。 二、未滿十四歲入國，每年居住二百七十日以上。 三、在我國出生，曾在我國合法累計居留十年，每年居住一百八十三日以上。 前項外國人應於居留期限屆滿前三個月內，檢具下列文件及照片一張，向移民署申請： 一、申請書。 二、護照及外僑居留證。 三、親屬關係證明。 四、其他相關證明文件。 第二項之外國人於本辦法中華民國一百十年七月九日修正發布，一百十二年一月一日施行前未滿十六歲入國者，得適用修正施行前之規定，不受該項第二款有關未滿十四歲入國之限制。 

 第 10 條 
 外國人來臺投資，或依就業服務法第四十六條第一項第一款至第七款、第四十八條第一項第一款、第三款應聘來臺，或從事外國專業人才延攬及僱用法第四條第四款第三目至第五目、第八條至第十一條之專業工作，或經外交部專案許可居留，於居留期限屆滿前，本人、其原經許可居留之配偶、未滿十八歲子女及年滿十八歲因身心障礙無法自理生活之子女，得向移民署申請延期居留。 依前項規定申請延期居留經許可者，其外僑居留證之有效期間自原居留期限屆滿之翌日起延期六個月；延期屆滿前，有必要者，得再申請延期居留一次，總延期居留期間最長為一年。 

 第 11 條 
 來臺就學之外國人畢業後，於居留期限屆滿前，本人、其原經許可居留之配偶、未滿十八歲子女及年滿十八歲因身心障礙無法自理生活之子女，得向移民署申請延期居留。 依前項規定申請延期居留經許可者，其外僑居留證之有效期間自原居留期限屆滿之翌日起延期一年；延期屆滿前，有必要者，得再申請延期居留一次，總延期居留期間最長為二年。 

 第 12 條 
 下列外國人之外僑居留證，其有效期間最長不得逾一年： 一、在大專校院附設之華語文中心學習語文或在短期補習班研習華語之人員。 二、經教育或其他有關主管機關核准，在我國研習、受訓之人員。 三、外籍傳教及弘法人士。 四、與現在在臺灣地區居住且設有戶籍國民結婚，初次申請依親居留者。 五、其他有居留需要之人員。 第九條第二項外國人申請延期居留經許可核發之外僑居留證，其有效期間自原居留期限屆滿之翌日起延期三年，必要時，得再申請延期居留一次，期間不得逾三年。 

 第 13 條 
 外國人以依親為居留原因取得之外僑居留證，以其所依親屬之居留期限為居留期限，其所依親屬為我國國民者，外僑居留證有效期間最長不得逾三年。 

 第 14 條 
 外國人居留期限屆滿，或居留原因消失，經廢止居留許可，有第三條第二項但書各款情形之一者，得提出相關證明文件，向移民署申請延長出國期限。 前項所定出國期限，準用第三條第三項規定。 

 第 15 條 
 外國人申請永久居留，應檢具下列文件及照片一張，向移民署申請，經許可者，核發外僑永久居留證： 一、申請書。 二、護照。 三、外僑居留證。 四、健康檢查合格證明。 五、足以自立之財產或特殊技能證明。 六、最近五年內之本國及我國警察刑事紀錄證明。 七、其他相關證明文件。 依本法第二十五條第三項及第四項規定申請永久居留者，應另檢附經中央目的事業主管機關或經認可機構核發之證明文件；其與依本法第二十五條第五項規定隨同申請者，免附前項第三款、第五款及第六款文件。 外國人申請永久居留，於最近五年期間，每次出國在三個月以內者，得免附第一項第四款文件及第六款之本國警察刑事紀錄證明。 第一項第四款所定健康檢查合格證明之檢查項目，依中央衛生主管機關訂定之健康檢查證明應檢查項目表辦理。 外國人經依本法第三十三條第四款規定註銷外僑永久居留證，仍具有居留資格者，得於註銷之日起算三十日內申請居留。 

 第 16 條 
 外國人申請在我國投資移民，有下列情形之一者，移民署得准予永久居留： 一、投資金額新臺幣一千五百萬元以上之營利事業，並創造五人以上之本國人就業機會滿三年。 二、投資中央政府公債面額新臺幣三千萬元以上滿三年。 

 第 17 條 
 外國人申請居留、變更居留原因、延期居留或永久居留，有本法第二十四條第一項各款情形之一者，移民署得不予許可；已許可者，得撤銷或廢止其許可，並註銷其外僑居留證或外僑永久居留證。 以依親為居留原因經許可居留，其依親對象出國（境）已逾二年，經移民署通知之日起算逾二個月仍未入國（境）者，得廢止其許可，並註銷其外僑居留證。 

 第 18 條 
 十四歲以上之外國人在我國境內應依本法第二十八條第一項規定，隨身攜帶護照、外僑居留證或外僑永久居留證。 無前項證件者，應攜帶經主管機關認定之其他身分證明文件。 

 第 19 條 
 居住臺灣地區設有戶籍國民持外國護照入國，申請延期停留、居留或延期居留者，應先至戶政事務所辦理戶籍遷出登記，移民署始得受理其申請。 尚未履行兵役義務之接近役齡男子或役齡男子，有下列情形之一者，移民署不受理其前項申請： 一、未持有役政用華僑身分證明書。 二、僑民役男居住臺灣地區屆滿一百八十三日。 三、依法應接受徵兵處理，並經限制出境。 

 第 20 條 
 外國人於居留期間內，有出國後再入國之必要者，應依本法第三十四條規定，於出國前向移民署申請核發重入國許可。申請核發外僑居留證之同時，亦得申請核發重入國許可。 前項重入國許可為多次使用，其有效期間不得逾外僑居留證之有效期間。 外僑居留證經註銷者，其重入國許可視同註銷。 經許可永久居留之外國人得持憑外僑永久居留證及有效護照重入國。 

 第 21 條 
 外國人停留或居留原因消失，經目的事業主管機關或相關機關查獲或知悉者，應通報移民署。 

 第 22 條 
 外國人在我國境內死亡，由其關係人或其本國駐臺使領館或授權機構於十五日內，向移民署辦理登記或由移民署查明後逕為登記。 法院、醫療機構、檢察機關、軍事檢察機關作成外國人之死亡資料後，應以網路分別傳輸司法院、衛生福利部、法務部、國防部，其接獲通報後，應再以網路傳輸內政部，並由移民署辦理登記。 前項外國人之死亡資料及其傳輸期限，準用死亡資料通報辦法第二條及第四條規定。 移民署依第一項或第二項規定辦理登記後，應即將登記事項通知其遺產稅中央政府所在地之主管稅捐稽徵機關。 

 第 23 條 
 外國人因原發照國家或其他國家拒絕接納其入國、罹患重大疾病或其他特殊原因而無法執行強制驅逐出國者，得在限定其住居所或附加其他條件後，核發臨時外僑登記證。 

 第 24 條 
 本辦法施行日期，由內政部定之。 

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
 1,529,824,216人 

 本月瀏覽人次 
 5,288,334人 

 目前使用人次 
 1,631人 

 電子報訂閱人數 
 221,218人 

 本網站係提供法規之最新動態資訊及資料檢索，並不提供法規及法律諮詢之服務。 
 若有任何法律上的疑義，建議您可逕向發布法規之主管機關洽詢。 
 本網站法規資料係由政府各機關提供之電子檔或書面文字登打製作，若與各法規主管機關之公布文字有所不同，仍以各法規主管機關之公布資料為準。 
 部分資料內容，使用特殊文字或符號，如欲詳閱內容，請連結至 司法院網站 下載造字檔。 
 全國法規資料庫之內容每週五定期更新，當週發布之法律、命令資料，將於完成法規整編作業後，於下週五更新上線。 
 法規整編資料截止日：民國 115 年 01 月 09 日 
 瀏覽人次總計：1,529,824,216人 
 本月瀏覽人次：5,288,334人 
 目前使用人次：1,631人 
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
