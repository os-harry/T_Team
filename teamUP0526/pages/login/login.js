// pages/login/login.js
var app=getApp();

Page({
  //表单提交
  formSubmit: function (e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value);
    wx.request({
      url: ' ',//在这里加上后台的php地址
      data: { //发送给后台的数据
        'student_name':e.detail.value.student_name,
        'student_id': e.detail.value.student_id
      },
      method: 'POST',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      success: function (res) { //获取php的返回值res，res里面要有一个state和一个info，如果成功就在info里说成功，下面的弹窗会提醒。
        if (res.data.state == 1) {
          app.globalData.student_id = e.detail.value.student_id; //改变公共变量学生学号
          wx.navigateTo({ //跳转到个人首页
            url: '../class_list/class_list',
          });
        } else {
          wx.showToast({
            title: res.data.info
          });
        }
      }
    })
  },


  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})