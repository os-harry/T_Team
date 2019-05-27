// pages/class_join/class_join.js
var app=getApp();
Page({
  data:{

  },
  //表单提交
  formSubmit: function (e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
    wx.request({
      url: ' ',//在这里加上后台的php地址
      data: { //发送给后台的数据
        'class_invite_id': e.detail.value.invite_id,
      },
      method: 'POST',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      success: function (res) { //获取php的返回值res，res里面要有一个state和一个info，如果成功就在info里说成功，下面的弹窗会提醒,不成功给出原因的info返回，比如邀请码错误。
        if (res.data.state == 1) {
          app.globalData.class_id = res.data.class_id;  //更新全局变量中的class_id
          wx.navigateTo({ //跳转到班级首页
            url: '../team_list/team_list',
          });
        } else {
          wx.showToast({  //弹窗提醒邀请码错误
            title: res.data.info
          });
        }
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
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