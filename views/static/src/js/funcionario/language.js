function applyTranslations(i18n, locale) {
  // Assuming you have a function to select elements by their data-i18n-key
  //const selectElement = key => document.querySelector(`[data-i18n-key="${key}"]`);

  // Set translations for content1
  //selectElement('APP_NAME').textContent = i18n['APP_NAME'];
  //selectElement('GENERAL.MESSAGE_BOX').textContent = i18n['GENERAL']['MESSAGE_BOX'];
  //selectElement('GENERAL.DESCRIPTION_BOX').textContent = i18n['GENERAL']['DESCRIPTION_BOX'];
  //alert(i18n['APP_NAME']);
}


function ReceiveString(i18n) {
  const language = {
    AppName: i18n.APP_NAME,
    warningBefore: i18n.GENERAL.WARNING_BEFORE,
    warningAfter: i18n.GENERAL.WARNING_AFTER,
    acceptButton: i18n.GENERAL.ACCEPT,
    declineButton: i18n.GENERAL.DECLINE,
    msgWorkStart: i18n.GENERAL.WORK_START,
    msgWorkPause: i18n.GENERAL.WORK_PAUSE,
    msgWorkReturn: i18n.GENERAL.WORK_RETURN,
    msgWorkEnd: i18n.GENERAL.WORK_END,
    msgBeforeStart: i18n.GENERAL.BEFORE_START,
    msgBeforePause: i18n.GENERAL.BEFORE_PAUSE,
    msgBeforeReturn: i18n.GENERAL.BEFORE_RETURN,
    msgBeforeEnd: i18n.GENERAL.BEFORE_END,
    msgAfterStart: i18n.GENERAL.AFTER_START,
    msgAfterPause: i18n.GENERAL.AFTER_PAUSE,
    msgAfterReturn: i18n.GENERAL.AFTER_RETURN,
    msgAfterEnd: i18n.GENERAL.AFTER_END,
    msgAbnormalOn: i18n.GENERAL.ABNORMAL_ON,
    msgAbnormalOff: i18n.GENERAL.ABNORMAL_OFF,
    msgTermsService: i18n.GENERAL.TERMS_SERVICE,
    enUsButton: i18n.GENERAL.EN_US_BUTTON,
    ptBrButton: i18n.GENERAL.PT_BR_BUTTON,
    ruRuButton: i18n.GENERAL.RU_RU_BUTTON,
    esEsButton: i18n.GENERAL.ES_ES_BUTTON,
    locale: i18n.LOCALE
  };

  return language;
}
